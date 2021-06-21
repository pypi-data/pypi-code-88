# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging

from azureml.core import RunConfiguration

from azureml.responsibleai.tools.interpret._api.surrogate_types import SurrogateTypes


logger = logging.getLogger(__name__)


EXPLANATION_DEPENDENCIES = [
    'azureml-core',
    'azureml-dataset-runtime',
    'azureml-responsibleai',
    'azureml-interpret',
]


def inject_dependencies(
    run_config: RunConfiguration,
    surrogate_type: str,
) -> None:
    """
    Update the RunConfiguration with the Python packages required to explain a model.

    :param run_config: The RunConfiguration to update.
    :param surrogate_type: The name of the surrogate model to use when explaining.
    """
    conda_deps = run_config.environment.python.conda_dependencies

    required_dependencies = []
    required_dependencies.extend(EXPLANATION_DEPENDENCIES)
    required_dependencies.extend(SurrogateTypes.get_dependencies(surrogate_type))

    did_inject = False
    for dependency in required_dependencies:
        if not any(dependency in package for package in conda_deps.pip_packages):
            message = ("The dependency {} is required to launch the remote model explanation. "
                       "Injecting it into the RunConfiguration.").format(dependency)
            logger.warning(message)
            conda_deps.add_pip_package(dependency)
            did_inject = True
    if not did_inject:
        logger.info("All remote model explanation dependencies were satisfied.")
