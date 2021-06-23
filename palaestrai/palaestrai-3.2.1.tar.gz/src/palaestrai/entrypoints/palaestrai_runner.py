import asyncio
from typing import Union, TextIO, Tuple, Any

from palaestrai.core import RuntimeConfig
from palaestrai.experiment import ExperimentRun, Executor, ExecutorState


def execute(
    experiment_run_definition: Union[ExperimentRun, TextIO, str],
    runtime_config: Union[str, TextIO, dict, None] = None,
) -> Tuple[str, ExecutorState]:
    """Provides a single-line command to start an experiment and set a
    runtime configuration

    Parameters
    ----------
    experiment_run_definition: 1. Already set ExperimentRun object
                               2. Any text stream
                               3. The path to a file
        The configuration from which the experiment is loaded.

    runtime_config:            1. Any text stream
                               2. dict
                               3. None
        The Runtime configuration applicable for the run.
        Note that even when no additional source is provided, runtime will load
        a minimal configuration from build-in defaults.

    Returns
    -------
    Experiment.user_id:  Unique experiment ID of type str
    executor state: The state the executor is now in of type ExecutorState
    """
    if runtime_config:
        RuntimeConfig().load(runtime_config)
    else:
        RuntimeConfig().load()

    if not isinstance(experiment_run_definition, ExperimentRun):
        experiment = ExperimentRun.load(experiment_run_definition)
    else:
        experiment = experiment_run_definition

    executor = Executor()
    executor.schedule(experiment)
    executor_final_state = asyncio.run(executor.execute())

    return experiment.user_id, executor_final_state
