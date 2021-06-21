"""
Field generator module.
"""

import argparse

from rpgt.src.setup.field.dl_setup import DLSetup
from rpgt.src.setup.field.field_setup import FieldSetup
from rpgt.src.setup.field.ml_setup import MLSetup
from rpgt.src.setup.field.rl_setup import RLSetup


def get_field(name: str, args: argparse.Namespace, cwd: str) -> FieldSetup:
    """
    Get field setup.
    :return: the field setup.
    """
    field_setup: FieldSetup
    # Field
    if name == "RL":
        field_setup = RLSetup(args, cwd)
    elif name == "DL":
        field_setup = DLSetup(args, cwd)
    elif name == "ML":
        field_setup = MLSetup(args, cwd)
    else:
        raise Exception(f"'{name}' is not supported as a field")

    return field_setup
