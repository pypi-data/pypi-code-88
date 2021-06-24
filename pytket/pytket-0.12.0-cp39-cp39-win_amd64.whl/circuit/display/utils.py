"""Functions and template filters used for displaying circuits."""

from typing import List, Tuple, Optional, Dict, Union
from typing_extensions import TypedDict

from pytket._tket.circuit import (  # type: ignore
    Circuit,
    Command,
    Op,
    QControlBox,
    CircBox,
    BitRegister,
    QubitRegister,
    Bit,
    Qubit,
)

# Type synonyms
Arg = Tuple[int, Union[int, bool]]
OutcomeArray = Union[BitRegister, QubitRegister]
Register = Union[Bit, Qubit]
ParsedOperation = TypedDict(
    "ParsedOperation",
    {
        "op": Dict[str, Union[str, Optional[Op]]],
        "params": str,
        "args": List[Arg],
        "n_args": int,
    },
)
ParsedCircuit = TypedDict(
    "ParsedCircuit",
    {
        "bits": List[Register],
        "qubits": List[Register],
        "layers": List[List[ParsedOperation]],
    },
)


def format_complex_number(real: float, imag: float) -> str:
    """Get a string to display a given complex number nicely"""
    str_imag = "" if imag == 0 else str(round(abs(imag), 3)) + "i"
    str_real = "" if real == 0 else str(round(real, 3))
    sign = "0" if real == 0 and imag == 0 else " + " if real * imag != 0 else ""
    # if both are defined, move imag's sign to sign.
    if real != 0 and imag < 0:
        sign = " - "

    return "{}{}{}".format(str_real, sign, str_imag)


def print_bitstring(width: int, bitset: List[int]) -> str:
    """Format and print a bitset of a certain width with padding."""
    return "".join(map(lambda x: bin(x)[2:].zfill(8)[:width], bitset))


def get_states_from_outcomearray(outcome_array: OutcomeArray) -> List[str]:
    """Get a list of strings representing the states associated
    with an outcome array."""
    return list(map(lambda x: print_bitstring(outcome_array.size, x), outcome_array))


def get_first_state_from_outcomearray(outcome_array: OutcomeArray) -> str:
    """Get a string representing the first state associated with an outcome array."""
    return print_bitstring(outcome_array.size, outcome_array[0])


def is_control_gate(op_type: str) -> bool:
    """Get whether a gate type includes a control (q)bit."""
    return op_type in {
        "CX",
        "CY",
        "CZ",
        "CH",
        "CRz",
        "CU1",
        "CU3",
        "CSWAP",
        "CnRy",
        "CnX",
        "CCX",
        "Control",
        "Condition",
    }


def get_target_args(args: List[Arg]) -> List[Arg]:
    """Given args for a controlled operation, get the args that are being acted on"""
    return [arg for arg in args if arg[0] < 2 and arg[1] > -1]


def get_op_name(op_type: str, operation: Optional[Op]) -> str:
    """Get the display name of the circuit operation."""

    def convert(control_type: str, op: Optional[Op]) -> Tuple[str, Optional[Op]]:
        if op is not None:
            if control_type in {"CX", "CY", "CZ", "CH", "CRz", "CU1", "CU3", "CSWAP"}:
                return op.type.name[1:], None
            elif control_type in {"CCX", "CnRy", "CnX"}:
                return op.type.name[2:], None
            elif control_type == "Control" and isinstance(op.box, QControlBox):
                return op.box.op.type.name, op.box.op
            elif control_type == "Condition" and op.conditional is not None:
                return op.conditional.op.type.name, op.conditional.op
            elif control_type == "CircBox" and isinstance(op.box, CircBox):
                name = getattr(op.box.circuit, "name", "Custom Circuit")
                return name, None

        return "Custom", None

    while is_control_gate(op_type) or op_type == "CircBox":
        op_type, operation = convert(op_type, operation)

    return op_type


# Controlled operations get special treatment:
# List obtained from https://cqcl.github.io/pytket/build/html/optype.html
def get_controlled_ops(op_type: str, command: Command) -> int:
    """Return the number of control bits involved in a given controlled operation"""
    if op_type in {"CX", "CY", "CZ", "CH", "CRz", "CU1", "CU3", "CSWAP"}:
        return 1
    elif op_type in {"CnRy", "CnX"}:
        return len(command.args) - 1
    elif op_type == "CCX":
        return 2
    elif op_type == "Control" and isinstance(command.op.box, QControlBox):
        return int(command.op.box.n_controls)
    elif op_type == "Condition" and command.op.conditional is not None:
        return int(command.op.conditional.width)

    return 0


def make_operation(
    args: List[Arg],
    params: Optional[list] = None,
    op_type: Optional[str] = "ID",
    raw_op: Optional[Op] = None,
) -> ParsedOperation:
    """Construct an operation from a command"""
    if params is None:
        params = []
    return {
        "op": {"type": op_type, "raw": raw_op},
        "params": "(" + ", ".join(map(str, params)) + ")" if len(params) > 0 else "",
        "args": args,
        "n_args": len(args),
    }


# Prepare a circuit for the templates
def parse_circuit(raw_circuit: Circuit) -> ParsedCircuit:
    """We pre-process the raw circuit for display:
    - Break the circuit down into a grid, displayed as a sequence
        of stacked blocks.
    - Each block is either an identity wire on the relevant (qu)bit,
        or [part of] a command.
    - The circuit is split into a list of (vertical) layers, each
        of which is a list of operations.
    - So each layer contains a command, possibly surrounded by
        identities on either side.
    - Each layer involves each qubit exactly once, and defines
        which blocks are to be rendered for that column.
    """
    parsed_circuit = ParsedCircuit(
        bits=raw_circuit.bits,
        qubits=raw_circuit.qubits,
        layers=[],
    )

    # Note: arg format is (type, pos) where:
    # - type: bit = 0, qubit = 1, control bit = 2, control qubit = 3
    # - link: -1 if not included, otherwise the position in the operation.

    # Start with a layer of identities.
    id_layer = [
        make_operation(
            [(1, 1) for qubit in raw_circuit.qubits]
            + [(0, 1) for bit in raw_circuit.bits]
        )
    ]
    parsed_circuit["layers"].append(id_layer)

    # Create a layer for each command.
    # We try to collapse layers together where we can.
    pos = 0  # keep track of which register we have filled the layer up to.
    layer = []
    registers = parsed_circuit["qubits"] + parsed_circuit["bits"]
    for command in raw_circuit.get_commands():
        # Go through each register and allocate it to the argument list for the
        # appropriate operation:
        # - Id until we get to the first (qu)bit featuring in the command
        # - and Id after we have covered the last (qu)bit in the command.
        # Identify the boundaries:
        sorted_args = sorted(command.args, key=registers.index)
        q_index = {
            "min": registers.index(sorted_args[0]),
            "max": registers.index(sorted_args[-1]),
        }

        args_top = []
        args_command = []

        # If we can't fit this command onto the current layer,
        # fill the previous with ids and prepare the next layer:
        if q_index["min"] < pos:
            # pad the rest our with ids and add the layer in.
            layer.append(
                make_operation(
                    [
                        (1 if i < len(parsed_circuit["qubits"]) else 0, 1)
                        for i in range(pos, len(registers))
                    ]
                )
            )
            parsed_circuit["layers"].append(layer)
            # reset the layer and pos
            layer = []
            pos = 0

        for i in range(pos, q_index["max"] + 1):
            register, n_is_quantum = (
                registers[i],
                1 if i < len(parsed_circuit["qubits"]) else 0,
            )

            # if this is a controlled operation, alter the wire type accordingly
            if is_control_gate(command.op.type.name):
                n_control = get_controlled_ops(command.op.type.name, command)
                if registers[i] in command.args[:n_control]:
                    n_is_quantum += 2

            if i < q_index["min"]:  # top id section
                args_top += [(n_is_quantum, 1)]
            elif i < q_index["max"] + 1:  # part of/overlapping the command
                args_command += [
                    (
                        n_is_quantum,
                        -1
                        if register not in command.args
                        else command.args.index(register),
                    )
                ]

        # Add the (up to) 3 operations to our layer:
        if len(args_top) > 0:
            layer.append(make_operation(args_top))
        if len(args_command) > 0:
            layer.append(
                make_operation(
                    args_command,
                    params=command.op.params,
                    op_type=command.op.type.name,
                    raw_op=command.op,
                )
            )

        pos = q_index["max"] + 1

    # If we have a leftover layer, add it in
    if len(layer) > 0:
        # pad the rest our with ids and add the layer in.
        layer.append(
            make_operation(
                [
                    (1 if i < len(parsed_circuit["qubits"]) else 0, 1)
                    for i in range(pos, len(registers))
                ]
            )
        )
        parsed_circuit["layers"].append(layer)

    # Add a layer of id at the end of the circuit
    parsed_circuit["layers"].append(id_layer)
    return parsed_circuit
