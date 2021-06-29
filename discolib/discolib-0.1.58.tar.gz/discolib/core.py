from discolib.attr import DiscoAttribute
from discolib.io import DiscoIO

from typing import List
import json

class Disco:
    """Houses all attributes and interaction functions."""
    def _cmd_to_port(self, cmd, port) -> bytes:
        """Send a byte command (without data) to a port."""
        data = bytes([0x42, 0x42, 0x03, cmd, port, 0x10])
        self._io.write(data)
        resp = self._io.read_response()
        return resp

    def _get_ports(self) -> List:
        """Retrieve all ports and the attributes they represent."""
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
        """Initialize all attributes and construct their accessors."""
        self._io = io_handler
        self._attrs = []
        self._attr_dicts = []
        for port in self._get_ports():
            attr = DiscoAttribute(port['port'], port['type'], port['name'], self._io)
            setattr(self, attr.name, attr)
            self._attr_dicts.append(attr.serialize(ignore_protected=True))

    def get_attrs(self) -> List:
        """Retrieve a list of all attribute objects."""
        return self._attrs

    def get_attr_dicts(self) -> List:
        """Retrieve a list of dictionary representations of each attribute."""
        return self._attr_dicts

    def get_attr_json(self, indent=None) -> str:
        """Retrieve a json string representation of all attributes."""
        return json.dumps(self._attr_dicts, indent=indent)

