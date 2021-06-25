#!/usr/bin/env python
# coding: utf-8

# Copyright (c) CoSApp Team.


"""
Widget container as geometry viewer panel
"""
from collections import OrderedDict
from typing import Any, Callable, Dict, List, Union
from weakref import ReferenceType

from cosapp.recorders import DataFrameRecorder
from cosapp.systems import System
from cosapp_lab.widgets.utils import CosappObjectParser, OccParser
from cosapp_lab.widgets.base.base_component import BaseComponent


class GeometryComponent(BaseComponent):
    name = "GeometryView"

    def __init__(
        self,
        data: "ReferenceType[System]",
        sys_data: CosappObjectParser,
        send_func: Callable,
        add_shape=None,
        source=None,
        **kwargs
    ):
        super().__init__(data=data, sys_data=sys_data, send_func=send_func, **kwargs)

        self.add_shape = add_shape
        self.geo_source = source
        self.time_step = 0
        self.__init_connection()

    def __init_connection(self):
        """Initialize the connection between fontend - backend and
        between input system with the callbacks.
        """
        if self.geo_source is not None and "recorder" in self.geo_source:
            self._static = False
            path_list = self.geo_source["recorder"].split(".")
            driver_name = path_list[-1]
            if len(path_list) == 1:
                recorder = self.system.drivers[driver_name].recorder
            else:
                recorder = (
                    self.system[".".join(path_list[0:-1])]
                    .drivers[driver_name]
                    .recorder
                )
            recorder.state_recorded.connect(self.save_data)
        else:
            driver_list = self.sys_data.get_time_driver()
            if len(driver_list) > 0:
                self._static = False
                time_driver = driver_list[0]
                if time_driver.recorder is not None:
                    time_driver.recorder.state_recorded.connect(self.save_data)
                else:
                    notification_recorder = time_driver.add_recorder(
                        DataFrameRecorder(includes=["_"])
                    )
                    notification_recorder.state_recorded.connect(self.save_data)
            else:
                self._static = True

    def save_data(self, **kwarg) -> None:
        """Callback function used to get geometry data
        after each time step.
        """
        data: OccParser = self.get_geometry(self.system)
        threejs_data = data.threejs_data
        binary_data = []
        binary_position = data.binary_position

        for b_data in data.binary_data:
            binary_data.append(b_data.tobytes())
        payload = {
            "threejs_data": threejs_data,
            "binary_position": binary_position,
            "time_step": self.time_step,
        }
        self.send({"type": "GeometryView::geo_data", "payload": payload}, binary_data)
        self.time_step += 1

    def send_initial_geometry(self) -> None:
        if self.geo_source is not None and "recorder" in self.geo_source:
            all_data = self.get_geometry(self.system, get_all=True)
            payload_length = len(all_data)
            for idx in all_data:
                payload_length -= 1
                threejs_data = all_data[idx].threejs_data
                binary_data = []
                binary_position = all_data[idx].binary_position
                for b_data in all_data[idx].binary_data:
                    binary_data.append(b_data.tobytes())
                payload = {
                    "threejs_data": threejs_data,
                    "binary_position": binary_position,
                    "time_step": idx,
                    "remaining": payload_length,
                }
                self.send(
                    {"type": "GeometryView::geo_data", "payload": payload}, binary_data
                )
        else:

            data = self.get_geometry(self.system)
            threejs_data = data.threejs_data
            binary_data = []
            binary_position = data.binary_position
            if len(threejs_data) > 0:
                for b_data in data.binary_data:
                    binary_data.append(b_data.tobytes())
                payload = {
                    "threejs_data": threejs_data,
                    "binary_position": binary_position,
                    "time_step": 0,
                    "remaining": 0,
                }
                self.send(
                    {"type": "GeometryView::geo_data", "payload": payload}, binary_data
                )

    def get_geometry(
        self, sys: System, get_all=False
    ) -> Union[
        OccParser, Dict[int, OccParser]
    ]:  # Dict[int, List[Dict[str, List[Union[int, float]]]]]:
        """Convert the open cascade object inside system into
        serializable data in order to send to front end.

        Parameters
        ----------
        sys : System
            The input system.

        Returns
        -------
        Dict[int, List[Dict[str, List[Union[int, float]]]]]
            A dictionary contains geometry data.
        """

        if self.geo_source is not None and "recorder" in self.geo_source:

            path_list = self.geo_source["recorder"].split(".")
            driver_name = path_list[-1]
            if len(path_list) == 1:
                recorder = self.system.drivers[driver_name].recorder
            else:
                recorder = (
                    self.system[".".join(path_list[0:-1])]
                    .drivers[driver_name]
                    .recorder
                )
            try:
                recorder_data = recorder.export_data()
            except:
                recorder_data = recorder.data
            n_index = len(recorder_data.index)
            if get_all:
                ret = OrderedDict()
                for idx in range(n_index):
                    r = []
                    for var_name in self.geo_source.get("variables", []):
                        column = recorder_data.get(var_name)
                        r.append(column[idx])
                    shape_data = OccParser(r)
                    ret[idx] = shape_data
                return ret
            else:
                r = []
                for var_name in self.geo_source.get("variables", []):
                    column = recorder_data.get(var_name)
                    r.append(column[n_index - 1])
                shape_data = OccParser(r)
                return shape_data

        else:

            r = []
            if self.add_shape is not None:

                self.add_shape(r, sys)
            else:
                try:
                    GeometryComponent.default_add_shape(r, sys)
                except:
                    pass

            shape_data = OccParser(r)
            return shape_data

    @staticmethod
    def default_add_shape(r: List, system: System) -> None:
        """Helper function used to extract all geometry inside
        system, it will be used if user defined function is not provided.

        Parameters
        ----------
        r : List
            The list contains all geometry variable of system.

        system : System
            The input system.

        """
        # TODO The method used to get shape from system should be generalized
        # in CosApp level instead of interface level.

        for child in system.children.values():
            GeometryComponent.default_add_shape(r, child)

        def filter_shapes(p: "ExtensiblePort") -> "bool":
            return (
                p.__class__.__name__ == "GeometryPort"
                and p.visible
                and p.shape is not None
            )

        for port in filter(filter_shapes, system.outputs.values()):
            if isinstance(port.shape, List):
                r.extend(port.shape)
            else:
                r.append(port.shape)

    def computed_notification(self) -> None:
        """Callback function used to update geometry data from buffer
        and to emit update signal to front end.
        """

        if self._static:
            data = self.get_geometry(self.system)
            threejs_data = data.threejs_data
            binary_data = []
            binary_position = data.binary_position
            if len(threejs_data) > 0:
                for b_data in data.binary_data:
                    binary_data.append(b_data.tobytes())
                payload = {
                    "threejs_data": threejs_data,
                    "binary_position": binary_position,
                    "time_step": 0,
                    "remaining": 0,
                }
                self.send(
                    {"type": "GeometryView::geo_data", "payload": payload}, binary_data
                )
        else:
            self.send(
                {
                    "type": "GeometryView::update_signal",
                    "payload": {},
                }
            )
            self.time_step = 0

    def _handle_button_msg(self, model: Any, content: Dict, buffers: List):
        if content["action"] == "GeometryView::requestInitialGeometry":
            self.send_initial_geometry()
