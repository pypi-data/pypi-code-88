import argparse
import copy
import logging
import random
import string

import yaml
from bayes_optim.search_space import Bool, Discrete, Integer, Ordinal, Real

from .operator import AbstractOperator

__authors__ = ["Hao Wang"]

# variable types for katib's YAML
_type_switch = {
    Real: "double",
    Integer: "int",
    Discrete: "categorical",
    Ordinal: "categorical",  # TODO: Katib does not support this for now..
    Bool: "categorical",  # TODO: Katib does not support this for now..
}

# part of the YAML file required by AIE-Katib
_partial_yaml = {
    "parameters": [],
    "trialTemplate": {
        "primaryContainerName": "training-container",
        "trialParameters": [],
        "trialSpec": {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "spec": {
                "template": {
                    "spec": {
                        "containers": [{"name": "training-container", "image": "", "command": []}],
                        "restartPolicy": "Never",
                    }
                }
            },
        },
    },
}


def _var_bounds_to_yaml(var):
    if isinstance(var, (Real, Integer)):
        out = {"min": str(var.bounds[0]), "max": str(var.bounds[1])}
        if hasattr(var, "step"):
            out["step"] = var.step
    elif isinstance(var, (Bool, Discrete, Ordinal)):
        out = {"list": list(map(str, var.bounds))}
    return out


def create_cmd_parser_from_operator(op: AbstractOperator):
    _vars = copy.copy(op.config_space.data)
    parser = argparse.ArgumentParser(
        # TODO: indeed, perhaps it is good to have an optional `description` attribute
        # for each operator
        description=op.__class__.__name__,
        prog="main.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    if hasattr(op, "target_metric"):
        parser.add_argument(
            "--target_metric",
            type=str,
            default=op.target_metric,
            help="the target metric used for hyperparameter optimization",
        )

    for var in _vars:
        parser.add_argument(
            f"--{var.name}",
            # NOTE: get the type of the range of the var.
            type=type(var.bounds[0]),
            default=var.default_value,
            help="",
        )
    return parser


def create_partial_yaml_from_operator(
    op: AbstractOperator,
    image_url: str = "",
    path_to_main: str = "",
    yaml_file: str = None,
) -> dict:
    """Generate a partial YAML file for Katib

    Parameters
    ----------
    op : AbstractOperator
        the ML model
    image_url : str, optional
        URL to the docker image containing model `op`, by default ''
    path_to_main : str, optional
        path to 'main.py' within the docker image, by default ''
    yaml_file : str, optional
        output YAML file, by default None

    Returns
    -------
    dict
        a dictionary corresponds to the YAML
    """
    if not path_to_main:
        path_to_main = f"opt/{type(op).__name__}"

    _vars = copy.copy(op.config_space.data)
    out = copy.copy(_partial_yaml)

    out["parameters"] = [
        {
            "name": var.name,
            "parameterType": _type_switch[type(var)],
            "feasibleSpace": _var_bounds_to_yaml(var),
        }
        for var in _vars
    ]
    out["trialTemplate"]["trialParameters"] = [
        {"name": var.name, "description": "", "reference": var.name} for var in _vars
    ]
    command = ["python", f"{path_to_main}/main.py"] + [
        f"--{var.name}=${{trialParameters.{var.name}}}" for var in _vars
    ]
    out["trialTemplate"]["trialSpec"]["spec"]["template"]["spec"]["containers"][0][
        "command"
    ] = command
    out["trialTemplate"]["trialSpec"]["spec"]["template"]["spec"]["containers"][0][
        "image"
    ] = image_url

    if hasattr(op, "metrics"):
        out["trialTemplate"]["trialSpec"]["spec"]["template"]["spec"]["containers"][0][
            "metrics"
        ] = [m.__name__ for m in op.metrics]

    if yaml_file:
        with open(yaml_file, "w") as f:
            yaml.dump(out, f, allow_unicode=True, default_flow_style=False)
    return out


def random_string(k: int = 15):
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


class LoggerFormatter(logging.Formatter):
    """logger for all operators"""

    FORMATS = {
        logging.DEBUG: "%(asctime)s - [%(levelname)s] {%(pathname)s:%(lineno)d} -- %(message)s",
        logging.INFO: "%(asctime)s - [%(levelname)s] {%(module)s} -- %(message)s",
        logging.WARNING: "%(asctime)s - [%(levelname)s] {%(name)s} -- %(message)s",
        logging.ERROR: "%(asctime)s - [%(levelname)s] {%(name)s} -- %(message)s",
        "DEFAULT": "%(asctime)s - %(levelname)s -- %(message)s",
    }

    def __init__(self, fmt="%(asctime)s - %(levelname)s -- %(message)s"):
        LoggerFormatter.FORMATS["DEFAULT"] = fmt
        super().__init__(fmt=fmt, datefmt=None, style="%")

    def format(self, record):
        # Save the original format configured by the user
        # when the logger formatter was instantiated
        _fmt = getattr(self._style, "_fmt")
        # Replace the original format with one customized by logging level
        setattr(self._style, "_fmt", self.FORMATS.get(record.levelno, self.FORMATS["DEFAULT"]))
        # Call the original formatter class to do the grunt work
        fmt = logging.Formatter.format(self, record)
        # Restore the original format configured by the user
        setattr(self._style, "_fmt", _fmt)
        return fmt
