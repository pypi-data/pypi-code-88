# Copyright 2019-2021 Cambridge Quantum Computing
#
# You may not use this file except in compliance with the Licence.
# You may obtain a copy of the Licence in the LICENCE file accompanying
# these documents or at:
#
#     https://cqcl.github.io/pytket/build/html/licence.html

""" BackendInfo class: additional information on Backends """
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Set, cast

from pytket.routing import Architecture, FullyConnected  # type: ignore
from pytket.circuit import OpType, Node  # type: ignore


@dataclass
class BackendInfo:
    """
    Stores various properties of a Backend.

    This provides all device information useful for compilation.

    :param name: Class name of the backend.
    :param device_name: Name of the device.
    :param version: Pytket-extension version installed when creating object.
    :param architecture: Device connectivity.
    :param gate_set: Set of supported gate types.
    :param supports_fast_feedforward: Flag for hardware support of fast feedforward.
    :param supports_reset: Flag for hardware support of reset operation
    :param supports_midcircuit_meas: Flag for hardware support of midcircuit
        measurement.
    :param misc: key-value map with further provider-specific information
    """

    # identifying information
    name: str
    device_name: Optional[str]
    version: str
    # hardware constraints
    architecture: Architecture
    gate_set: Set[OpType]
    # additional feature support
    supports_fast_feedforward: bool = False
    supports_reset: bool = False
    supports_midcircuit_measurement: bool = False
    # miscellaneous, eg noise characterisation and provider-supplied information
    misc: Dict[str, Any] = field(default_factory=dict)

    @property
    def nodes(self) -> List[Node]:
        """
        List of device nodes of the backend.

        :return: List of nodes.
        :rtype: List[Node]
        """
        return cast(List[Node], self.architecture.nodes)

    @property
    def n_nodes(self) -> int:
        """
        Number of nodes in the architecture of the device.

        :return: Number of nodes.
        :rtype: int
        """
        return len(self.nodes)

    def add_misc(self, key: str, val: Any) -> None:
        """
        Add a new entry in BackendInfo's dictionary of additional information.

        :param key: Key to store and retrieve value.
        :type key: str
        :param val: Value to be stored.
        """
        if key in self.misc:
            raise KeyError("Attempting to add an already existing entry to misc dict")
        self.misc[key] = val

    def get_misc(self, key: str) -> Any:
        """
        Retrieve information stored in Backend's additional information store

        :param key: Key to retrieve value.
        :type key: str

        :raises KeyError: There is no value stored with the given key.

        :return: The value stored at the given key.
        """
        return self.misc[key]

    def to_dict(self) -> Dict:
        """
        Get backend information serialised as a dict.

        :return: Dictionary output
        :rtype: Dict
        """
        self_dict = asdict(self)
        self_dict["architecture"] = self_dict["architecture"].coupling
        return self_dict

    @classmethod
    def from_dict(cls, d: Dict) -> "BackendInfo":
        """
        Construct BackendInfo object from serialised dict.

        :return: constructed BackendInfo object
        :rtype: BackendInfo
        """
        args = dict(**d)
        args["architecture"] = Architecture(args["architecture"])
        return cls(**args)


def fully_connected_backendinfo(  # type: ignore
    name: str,
    device_name: Optional[str],
    version: str,
    n_nodes: int,
    gate_set: Set[OpType],
    **kwargs
) -> BackendInfo:
    """
    Construct a BackendInfo with a FullyConnected architecture.

    :param name: Name of the device.
    :param version: Version of the pytket Backend.
    :param n_nodes: Number of nodes of the device.
    :param gate_set: Set of supported gate types.
    :param \\**kwargs: All further arguments are passed to the BackendInfo constructor.
    """
    return BackendInfo(
        name, device_name, version, FullyConnected(n_nodes), gate_set, **kwargs
    )
