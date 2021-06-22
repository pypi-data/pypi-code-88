from collections import Counter
import json
import typing
from typing import Any, Dict, Optional

from blueqat import Circuit
from bqbraket import convert
from bqbraket.backend import BASIS

from braket.device_schema import GateModelParameters
from braket.device_schema.ionq import IonqDeviceParameters
from braket.device_schema.rigetti import RigettiDeviceParameters
from braket.device_schema.simulators import GateModelSimulatorDeviceParameters
from braket.tasks import GateModelQuantumTaskResult

from ..data import ExecutionRequest
from ..abstract_result import AbstractResult

if typing.TYPE_CHECKING:
    from ..device import Device
    from ..task import CloudTaskOptions


def make_executiondata(c: Circuit, dev: 'Device', shots: int,
                       group: Optional[str], send_email: bool,
                       options: 'CloudTaskOptions') -> ExecutionRequest:
    """Make a request for the cloud server."""
    basis = ['cx']
    if options.get('transpile', True):
        if dev.value.startswith('IonQ'):
            basis = BASIS['ionq']
        elif dev.value.startswith('Aspen'):
            basis = BASIS['rigetti']
    else:
        basis = None
    action = convert(c, basis).to_ir().json()
    dev_params = make_device_params(c, dev)
    return ExecutionRequest(action, dev.value, dev_params, shots, group,
                            send_email)


def make_device_params(c: Circuit, dev: 'Device') -> str:
    """Make device parameters"""
    paradigm_params = GateModelParameters(qubitCount=c.n_qubits,
                                          disableQubitRewiring=False)
    if "/rigetti/" in dev.value:
        return RigettiDeviceParameters(
            paradigmParameters=paradigm_params).json()
    if "/ionq/" in dev.value:
        return IonqDeviceParameters(paradigmParameters=paradigm_params).json()
    if "/amazon/" in dev.value:
        return GateModelSimulatorDeviceParameters(
            paradigmParameters=paradigm_params).json()
    raise ValueError("Unknown AWS device.")


class BraketResult(AbstractResult):
    """Result of braket executed task"""
    def __init__(self, result_obj: Dict[str, Any]) -> None:
        jsonized = json.dumps(result_obj)
        self.result = GateModelQuantumTaskResult.from_string(jsonized)
        self.ordered_shots = None  # type: Optional[typing.Counter[str]]

    def _update_ordered_shots(self) -> None:
        n_qubits = self.result.task_metadata.deviceParameters.paradigmParameters.qubitCount
        if self.result.measured_qubits == list(range(n_qubits)):
            self.ordered_shots = self.result.measurement_counts
        else:
            measured = self.result.measured_qubits

            def conv(key):
                out = ['0'] * n_qubits
                for k, m in zip(key, measured):
                    out[m] = k
                return ''.join(out)

            self.ordered_shots = Counter({
                conv(k): v
                for k, v in self.result.measurement_counts.items()
            })

    def shots(self) -> typing.Counter[str]:
        if self.ordered_shots is None:
            self._update_ordered_shots()
        return self.ordered_shots


def make_result(data: Dict[str, Any], _: 'Device') -> Optional[BraketResult]:
    taskmetadata = data.get('taskMetadata')
    if not (taskmetadata and taskmetadata.get('id')):
        return None
    return BraketResult(data)
