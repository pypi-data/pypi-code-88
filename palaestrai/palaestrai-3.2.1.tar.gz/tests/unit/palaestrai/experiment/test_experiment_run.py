import os.path
import sys
import unittest
import uuid
from unittest.mock import MagicMock, patch

import pkg_resources
from palaestrai.experiment.experiment_run import ExperimentRun


class _UidentifiableMock(MagicMock):
    def __init__(self, id=None):
        super().__init__()
        self.uid = id if id else str(uuid.uuid4())


def load_with_params_side_effect(*args, **kwargs):
    return _UidentifiableMock()


@patch(
    "palaestrai.experiment.experiment_run.AgentConductor",
    MagicMock(side_effect=load_with_params_side_effect),
)
@patch(
    "palaestrai.experiment.experiment_run.load_with_params",
    MagicMock(side_effect=load_with_params_side_effect),
)
class TestExperimentRun(unittest.TestCase):
    def setUp(self):
        self.version = pkg_resources.require("palaestrai")[0].version
        self.dummy_exp_path = os.path.realpath(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "../../../fixtures/dummy_run.yml",
            )
        )
        self.schedule = [
            {
                "phase_0": {
                    "environments": [
                        {
                            "environment": {"name": "", "params": dict()},
                            "reward": {"name": "", "params": dict()},
                        }
                    ],
                    "agents": [
                        {
                            "name": "defender",
                            "brain": {"name": "", "params": dict()},
                            "muscle": {"name": "", "params": dict()},
                            "objective": {"name": "", "params": dict()},
                            "sensors": list(),
                            "actuators": list(),
                        },
                        {
                            "name": "attacker",
                            "brain": {"name": "", "params": dict()},
                            "muscle": {"name": "", "params": dict()},
                            "objective": {"name": "", "params": dict()},
                            "sensors": list(),
                            "actuators": list(),
                        },
                    ],
                    "simulation": {
                        "name": "",
                        "params": dict(),
                        "conditions": list(),
                    },
                    "phase_config": {"mode": "train", "worker": 1},
                }
            }
        ]
        self.run_config = {
            "condition": {
                "name": (
                    "palaestrai.experiment:"
                    "VanillaRunGovernorTerminationCondition",
                ),
                "params": dict(),
            }
        }

        self.schedule_p2 = {
            "phase_1": {
                "environments": [
                    {
                        "environment": {"name": "", "params": dict()},
                        "reward": {"name": "", "params": dict()},
                    }
                ],
                "agents": [
                    {
                        "name": "defender",
                        "brain": {"name": "", "params": dict()},
                        "muscle": {"name": "", "params": dict()},
                        "objective": {"name": "", "params": dict()},
                        "sensors": list(),
                        "actuators": list(),
                    },
                ],
                "simulation": {
                    "name": "",
                    "params": dict(),
                    "conditions": list(),
                },
                "phase_config": {"mode": "test", "worker": 1},
            }
        }
        self.schedule_p3 = {
            "phase_1": {
                "environments": [
                    {
                        "environment": {"name": "", "params": dict()},
                        "reward": {"name": "", "params": dict()},
                    }
                ],
                "agents": [
                    {
                        "name": "attacker",
                        "brain": {"name": "", "params": dict()},
                        "muscle": {"name": "", "params": dict()},
                        "objective": {"name": "", "params": dict()},
                        "sensors": list(),
                        "actuators": list(),
                    },
                ],
                "simulation": {
                    "name": "",
                    "params": dict(),
                    "conditions": list(),
                },
                "phase_config": {"mode": "train", "worker": 3},
            }
        }

    def test_properties(self):
        """Assert Not Empty list"""
        exp = ExperimentRun(
            user_id="test_properties",
            seed=123,
            version=self.version,
            schedule=self.schedule,
            run_config=self.run_config,
        )
        self.assertFalse(hasattr(exp, "schedule"))

    def test_setup_one_phase(self):
        """Assert setup"""
        exp = ExperimentRun(
            user_id="test_setup",
            seed=123,
            version=self.version,
            schedule=self.schedule,
            run_config=self.run_config,
        )
        exp.setup(broker_uri=None)
        self.assertEqual(len(exp.schedule_config), len(exp.schedule))
        self.assertEqual(1, len(exp.environment_conductors(0)))
        self.assertEqual(2, len(exp.agent_conductors(0)))
        self.assertEqual(1, len(exp.simulation_controllers(0)))

    def test_setup_three_phase(self):
        self.schedule.append(self.schedule_p2)
        self.schedule.append(self.schedule_p3)
        exp = ExperimentRun(
            user_id="test_setup",
            seed=123,
            version=self.version,
            schedule=self.schedule,
            run_config=self.run_config,
        )
        exp.setup(broker_uri=None)
        self.assertEqual(len(exp.schedule_config), len(exp.schedule))
        self.assertEqual(1, len(exp.environment_conductors(0)))
        self.assertEqual(2, len(exp.agent_conductors(0)))
        self.assertEqual(1, len(exp.simulation_controllers(0)))
        self.assertEqual(1, len(exp.environment_conductors(1)))

        # One agent was removed in phase 2
        self.assertEqual(1, len(exp.agent_conductors(1)))
        self.assertEqual(1, len(exp.simulation_controllers(1)))
        self.assertEqual(1, len(exp.environment_conductors(2)))
        self.assertEqual(1, len(exp.agent_conductors(2)))

        # Now we have three workers
        self.assertEqual(3, len(exp.simulation_controllers(2)))

    def test_load_from_file(self):
        exp = ExperimentRun.load(self.dummy_exp_path)
        self.assertFalse(hasattr(exp, "schedule"))

    def test_load_from_stream(self):
        with open(self.dummy_exp_path, "r") as stream_:
            exp = ExperimentRun.load(stream_)

        self.assertFalse(hasattr(exp, "schedule"))


class TestExperimentRunDump(unittest.TestCase):
    """Needed a separate test to get rid of the patches."""

    def test_dump(self):

        from io import StringIO

        import ruamel.yaml as yml
        from palaestrai.experiment import ExperimentRun

        dummy_exp_path = os.path.realpath(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "../../../fixtures/dummy_run.yml",
            )
        )
        sio = StringIO()
        yaml = yml.YAML(typ="safe")
        yaml.register_class(ExperimentRun)
        exp = ExperimentRun.load(dummy_exp_path)
        yaml.dump(exp, sio)

        exp_loaded = yaml.load(sio.getvalue())
        self.assertEqual(sys.getsizeof(exp), sys.getsizeof(exp_loaded))


if __name__ == "__main__":
    unittest.main()
