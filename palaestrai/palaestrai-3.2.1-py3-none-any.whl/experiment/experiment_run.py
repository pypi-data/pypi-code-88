"""This module contains the class :class:`ExperimentRun` that defines
an experiment run and contains all the information needed to execute
it.
"""
from __future__ import annotations

import collections.abc
from typing import TYPE_CHECKING, Dict, List, Union

from ..types.mode import Mode
from ..util import seeding
from ..util.exception import UnknownModeError

if TYPE_CHECKING:
    from palaestrai.simulation import SimulationController
    from palaestrai.experiment import TerminationCondition

import uuid

import pkg_resources
import ruamel.yaml as yml
from palaestrai.agent import AgentConductor
from palaestrai.environment import EnvironmentConductor
from palaestrai.util.dynaloader import load_with_params
from ruamel.yaml.constructor import ConstructorError

from . import LOG


class RunDefinitionError(RuntimeError):
    def __init__(self, run: ExperimentRun, message):
        super().__init__(message)
        self.message = message
        self.run = run

    def __str__(self):
        return "%s (%s)" % (self.message, self.run)


class ExperimentRun:
    """Defines an experiment run and stores information.

    The experiment run class defines a run in palaestrAI. It contains
    all information needed to execute the run. With the setup function
    the experiment run can be build.

    Parameters
    ----------

    """

    def __init__(
        self,
        user_id: Union[str, None],
        seed: Union[int, None],
        version: Union[str, None],
        schedule: List[Dict],
        run_config: dict,
    ):
        if seed is None:
            # numpy expects a seed between 0 and 2**32 - 1
            self.seed: int = seeding.create_seed(max_bytes=4)
        else:
            self.seed = seed

        if user_id is None:
            self.user_id = f"ExperimentRun-{uuid.uuid4()}"
            LOG.warning(
                "Experiment run has no user_id, please set one to "
                "identify it (assign the 'user_id' key). Generated: "
                "'%s', so that you can find it in the store.",
                self.user_id,
            )
        else:
            self.user_id = user_id

        palaestrai_version = pkg_resources.require("palaestrai")[0].version
        if version is None:
            self.version = palaestrai_version
            LOG.warning(
                "No version has been specified. There is no guarantee "
                "that this run will be executed without errors. Please "
                "set the version (assign the 'version' key) in the run "
                "file. Current palaestrAI version is '%s'.",
                self.version,
            )
        elif version != palaestrai_version:
            self.version = version
            LOG.warning(
                "Your palaestrAI installation has version %s but your "
                "run file uses version %s, which may be incompatible.",
                palaestrai_version,
                version,
            )
        else:
            self.version = version

        self.schedule_config = schedule
        self.run_config = run_config
        self.run_governor_termination_condition: TerminationCondition
        self.schedule: list

    def setup(self, broker_uri):
        """Set up an experiment run.

        Creates and configures relevant actors.
        """
        LOG.debug(
            "ExperimentRun(id=0x%x, user_id=%s) setup.", id(self), self.user_id
        )
        rgtc = self.run_config["condition"]
        LOG.debug(
            "ExperimentRun(id=0x%x, user_id=%s) loading RunGovernor "
            "TerminationCondition: %s.",
            id(self),
            self.user_id,
            rgtc["name"],
        )
        try:
            rgtc = load_with_params(rgtc["name"], rgtc["params"])
        except Exception as err:
            LOG.critical(
                "Could not load termination condition '%s' with params "
                "%s for RunGovernor: %s",
                rgtc["name"],
                rgtc["params"],
                err,
            )
            raise err
        self.run_governor_termination_condition = rgtc

        self.schedule = list()
        config = dict()
        for num, phase in enumerate(self.schedule_config):
            if len(phase) > 1:
                raise RunDefinitionError(
                    self,
                    (
                        "Only one phase per phase allowed but "
                        f"found {len(phase)} phases."
                    ),
                )
            elif len(phase) < 1:
                LOG.warning(
                    "ExperimentRun(id=0x%x, user_id=%s) found empty phase: "
                    "%d, skipping this one.",
                    id(self),
                    self.user_id,
                    num,
                )
                continue
            phase_name = list(phase.keys())[0]
            config = update_dict(config, phase[phase_name])
            agent_configs = dict()

            self.schedule.append(dict())
            self.schedule[num]["phase_config"] = config["phase_config"].copy()
            for env_config in config["environments"]:
                self.schedule[num].setdefault("environment_conductors", dict())

                ec = EnvironmentConductor(
                    env_config["environment"],
                    env_config["reward"],
                    broker_uri,
                    self.seed,
                )
                self.schedule[num]["environment_conductors"][ec.uid] = ec
            LOG.debug(
                "ExperimentRun(id=0x%x, uid=%s) set up %d "
                "EnvironmentConductor object(s) for phase %d: '%s'",
                id(self),
                self.user_id,
                len(self.schedule[num]["environment_conductors"]),
                num,
                phase_name,
            )
            if len(self.schedule[num]["environment_conductors"]) == 0:
                raise RunDefinitionError(
                    self, f"No environments defined for phase {num}."
                )

            for agent_config in config["agents"]:
                self.schedule[num].setdefault("agent_conductors", dict())

                ac_conf = {key: value for key, value in agent_config.items()}
                ac = AgentConductor(
                    broker_uri, ac_conf, self.seed, phase_name, str(id(self))
                )
                self.schedule[num]["agent_conductors"][ac.uid] = ac
                agent_configs[ac.uid] = ac_conf

            LOG.debug(
                "ExperimentRun(id=0x%x, user_id=%s) set up %d AgentConductor "
                "object(s) for phase %d: '%s'.",
                id(self),
                self.user_id,
                len(self.schedule[num]["agent_conductors"]),
                num,
                phase_name,
            )
            if len(self.schedule[num]["agent_conductors"]) == 0:
                raise RunDefinitionError(
                    self, f"No agents defined for phase {num}."
                )

            for _ in range(int(config["phase_config"].get("worker", 1))):
                self.schedule[num].setdefault("simulation_controllers", dict())
                try:
                    mode = Mode[
                        config["phase_config"].get("mode", "train").upper()
                    ]
                except KeyError as err:
                    raise UnknownModeError(err)

                sc: SimulationController = load_with_params(
                    config["simulation"]["name"],
                    {
                        "sim_connection": broker_uri,
                        "rungov_connection": broker_uri,
                        "agent_conductor_ids": self.schedule[num][
                            "agent_conductors"
                        ].keys(),
                        "environment_conductor_ids": self.schedule[num][
                            "environment_conductors"
                        ].keys(),
                        "termination_conditions": config["simulation"][
                            "conditions"
                        ],
                        "agents": agent_configs,
                        "mode": mode,
                    },
                )
                self.schedule[num]["simulation_controllers"][sc.uid] = sc
            LOG.debug(
                "ExperimentRun(id=0x%x, user_id=%s) set up %d "
                "SimulationController object(s) for phase %d: '%s'.",
                id(self),
                self.user_id,
                len(self.schedule[num]["simulation_controllers"]),
                num,
                phase_name,
            )
            if len(self.schedule[num]["simulation_controllers"]) == 0:
                raise RunDefinitionError(
                    self,
                    "No simulation controller defined. Either "
                    "'workers' < 1 or 'name' of key 'simulation' is "
                    "not available.",
                )
        LOG.info(
            "ExperimentRun(id=0x%x, user_id=%s) setup complete.",
            id(self),
            self.user_id,
        )

    def environment_conductors(self, phase=0):
        return self.schedule[phase]["environment_conductors"]

    def agent_conductors(self, phase=0):
        return self.schedule[phase]["agent_conductors"]

    def simulation_controllers(self, phase=0):
        return self.schedule[phase]["simulation_controllers"]

    def get_phase_name(self, phase: int):
        return list(self.schedule_config[phase].keys())[0]

    def get_episodes(self, phase: int):
        return self.schedule[phase]["phase_config"].get("episodes", 1)

    @property
    def num_phases(self):
        """The number of phases in this experiment run's schedule."""
        return len(self.schedule)

    def has_next_phase(self, current_phase):
        """Return if this run has a subsequent phase.

        Parameters
        ----------
        current_phase: int
            Index of the phase that is being executed.

        Returns
        -------
        bool
            True if at least one phase is taking place after
            the current phase.
        """
        return current_phase + 1 < self.num_phases

    @staticmethod
    def load(stream):
        LOG.debug("Loading configuration from %s.", stream)

        if isinstance(stream, str):
            try:
                stream = open(stream, "r")
            except OSError as err:
                LOG.error("Could not open run configuration: %s.", err)
                raise err
        try:
            conf = yml.YAML(typ="safe", pure=True).load(stream)
        except ConstructorError as err:
            LOG.error("Could not load run configuration: %s.", err)
            raise err
        finally:
            stream.close()
        LOG.debug("Loaded configuration: %s.", conf)

        return ExperimentRun(
            user_id=conf.get("user_id", conf.get("id", None)),
            seed=conf.get("seed", None),
            version=conf.get("version", None),
            schedule=conf["schedule"],
            run_config=conf["run_config"],
        )


def update_dict(src, upd):
    """Recursive update of dictionaries.

    See stackoverflow:

        https://stackoverflow.com/questions/3232943/
        update-value-of-a-nested-dictionary-of-varying-depth

    """
    for key, val in upd.items():
        if isinstance(val, collections.abc.Mapping):
            src[key] = update_dict(src.get(key, {}), val)
        else:
            src[key] = val
    return src
