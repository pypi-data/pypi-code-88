# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Notebook generation code used to generate Jupyter notebooks from a Jinja2 template."""
from typing import Any, Callable, List, Mapping, Dict, Set
import functools
import inspect
import json
import logging
import os
import pkg_resources

from azureml.train.automl.runtime import __version__
from azureml.core import Experiment
from azureml._common._error_definition import AzureMLError
from azureml.automl.core.shared._diagnostics.automl_error_definitions import AutoMLInternal
from azureml.automl.core.shared.exceptions import ClientException, ConfigException

import jinja2
from jinja2 import Environment, meta


PACKAGE_NAME = 'azureml.train.automl.runtime'
logger = logging.getLogger(__name__)


class NotebookTemplate:
    """
    Generates notebooks using a Jupyter notebook template.
    """

    def __init__(self, notebook_template: str) -> None:
        """
        Create an instance of a NotebookGenerator.

        :param notebook_template: the Jupyter notebook to use as a template, as a string
        """
        self.template = notebook_template

    @functools.lru_cache(maxsize=1)
    def get_arguments(self) -> Set[str]:
        """
        Retrieve the names of all the arguments needed to generate the notebook.

        :return: a list of all argument names
        """
        notebook = json.loads(self.template)
        env = Environment()
        args = set()  # type: Set[str]

        # Parse the contents of each notebook cell into an AST and scan for jinja2 variables
        for cell in notebook.get("cells", []):
            source = cell.get("source")
            if source:
                if isinstance(source, str):
                    stringified_source = source
                else:
                    stringified_source = "".join(source)
                parsed = env.parse(stringified_source)
                args |= meta.find_undeclared_variables(parsed)
        return args

    def generate_notebook(self, notebook_args: Dict[str, Any]) -> str:
        """
        Generate a notebook from a template using the provided arguments.

        :param notebook_args: a dictionary containing keyword arguments
        :return: a Jupyter notebook as a string
        """
        required_args = self.get_arguments()
        provided_args = set(notebook_args)
        missing_args = required_args - provided_args
        extra_args = provided_args - required_args

        logger.info("Unused arguments: {}".format(extra_args))

        if any(missing_args):
            raise ClientException._with_error(
                AzureMLError.create(
                    AutoMLInternal,
                    target="generate_notebook",
                    error_details="Mismatch between template and provided arguments. Missing arguments: {}".format(
                        missing_args
                    ),
                )
            )

        # Render the notebook template using the given arguments.
        # Arguments need to be escaped since Jupyter notebooks are in JSON format.
        env = Environment(undefined=jinja2.StrictUndefined)
        template = env.from_string(self.template)
        source = template.render(**{k: self.escape_json(notebook_args[k]) for k in notebook_args})

        # Tag the notebook with the SDK version used to generate it.
        node = json.loads(source)
        if "metadata" not in node:
            node["metadata"] = {}
        node["metadata"]["automl_sdk_version"] = __version__

        return json.dumps(node)

    @staticmethod
    def escape_json(input_str: Any) -> Any:
        """
        JSON escape a string. Other types are unaffected.

        :param input_str: the string
        :return: an escaped string, or original object if not a string
        """
        if not isinstance(input_str, str):
            return input_str
        return json.dumps(input_str).replace('/', r'\/')[1:-1]


def get_template(notebook_name: str) -> NotebookTemplate:
    """
    Load a notebook template from this package using its filename w/o extension.

    :param notebook_name:
    :return:
    """
    logger.info('Loading notebook {}'.format(notebook_name))
    template_path = pkg_resources.resource_filename(
        PACKAGE_NAME,
        os.path.join('_code_generation', 'notebook_templates', notebook_name + '.ipynb.template')
    )
    with open(template_path, 'r') as f:
        return NotebookTemplate(f.read())


def remove_matching_default_args(func: Callable[..., Any], args: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Given a function and function arguments, remove any arguments that match defaults in the function signature.

    :param func:
    :param args:
    :return:
    """
    signature = inspect.signature(func)

    # Ger all the default arguments from the function
    default_args = {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }

    # Only pick arguments if they either do not match a default argument or are not in the default argument list
    new_args = {
        k: v
        for k, v in args.items()
        if k not in default_args or v != default_args[k]
    }
    return new_args


def generate_script_run_notebook(experiment: Experiment) -> str:
    template_name = "script_run"
    template = get_template(template_name)
    logger.info('Notebook arguments: {}'.format(template.get_arguments()))

    workspace = experiment._workspace
    notebook = template.generate_notebook({
        'experiment_name': experiment.name,
        'workspace_name': workspace._workspace_name,
        'resource_group': workspace._resource_group,
        'subscription_id': workspace._subscription_id,
        'training_package': "azureml-automl-runtime~={}".format(__version__)
    })
    return notebook
