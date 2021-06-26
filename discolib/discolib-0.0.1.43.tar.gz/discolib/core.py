from discolib.attr import DiscoAttribute
from discolib.io import DiscoIO

import json

class Disco:

    def _cmd_to_port(self, cmd, port):
        data = bytes([0x42, 0x42, 0x03, cmd, port, 0x10])
        self._io.write(data)
        resp = self._io.read_response()
        return resp

    def _get_ports(self):
        data = bytes([0x42, 0x42, 0x2, 0x01, 0x10])
        self._io.write(data)
        resp = self._io.read_response()
        ports = list(resp)
        for port in ports:
            port_dict = {}
            port_dict['port'] = port
            resp = self._cmd_to_port(0x02, port)
            port_dict['name'] = resp.decode().strip('\x00')
            resp = self._cmd_to_port(0x03, port)
            port_dict['type'] = resp.decode()
            self._attrs.append(port_dict)
        return self._attrs

    def __init__(self, io_handler: DiscoIO) -> None:
        self._io = io_handler
        self._attrs = []
        self._attr_dicts = []
        for port in self._get_ports():
            attr = DiscoAttribute(port['port'], port['type'], port['name'], self._io)
            setattr(self, attr.name, attr)
            self._attr_dicts.append(attr.serialize(ignore_protected=True))

    def get_attrs(self) -> list:
        return self._attrs

    def get_attr_dicts(self) -> list:
        return self._attr_dicts

    def get_attr_json(self, indent=None) -> str:
        return json.dumps(self._attr_dicts, indent=indent)

