import logging
import random
import sys
import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, MagicMock, patch, call

from palaestrai.agent import RewardInformation
from palaestrai.agent.actuator_information import ActuatorInformation
from palaestrai.agent.sensor_information import SensorInformation
from palaestrai.core.protocol import (
    AgentSetupRequest,
    EnvironmentSetupRequest,
    EnvironmentStartRequest,
    EnvironmentStartResponse,
    EnvironmentUpdateResponse,
    SimulationControllerTerminationResponse,
)
from palaestrai.core.protocol.agent_update_rsp import AgentUpdateResponse
from palaestrai.core.serialisation import serialize
from palaestrai.simulation import VanillaSimControllerTerminationCondition
from palaestrai.simulation.vanilla_sim_controller import VanillaSimController
from palaestrai.types import Box, Discrete, Space


# from uuid import uuid4


def handle_client_msg(empf, message):

    if isinstance(message, EnvironmentSetupRequest):
        msg = serialize(
            EnvironmentUpdateResponse(
                "0",
                "0",
                "0",
                "0",
                [SensorInformation(1, Discrete(1), 0)],
                0.0,
                random.choice([True, False]),
            )
        )
        # print("returning msg")
        return msg

    elif isinstance(message, EnvironmentStartRequest):
        return serialize(
            EnvironmentStartResponse(
                0,
                0,
                [SensorInformation(1, Discrete(1), 0)],
                [
                    ActuatorInformation(
                        Discrete(1), Space.from_string("Discrete(2)"), 0
                    )
                ],
            )
        )
    elif isinstance(message, AgentSetupRequest):
        return serialize(
            AgentUpdateResponse(
                "0",
                "0",
                "0",
                [SensorInformation(1, Discrete(1), 0)],
                [
                    ActuatorInformation(
                        Discrete(1), Space.from_string("Discrete(2)"), 0
                    )
                ],
                [0.0],
            )
        )


class TestVanillaSimController(IsolatedAsyncioTestCase):
    def setUp(self):
        agent_dic = [
            {
                "name": "defender",
                "brain": {"name": "", "params": dict()},
                "muscle": {"name": "", "params": dict()},
                "objective": {"name": "", "params": dict()},
                "sensors": list(),
                "actuators": list(),
            },
        ]

        # uuid = uuid4()
        self.patch_client = (
            "palaestrai.simulation.simulation_controller.MajorDomoClient"
        )
        self.patch_worker = (
            "palaestrai.simulation.simulation_controller.MajorDomoWorker"
        )
        with patch(self.patch_worker, autospec=True):
            with patch(self.patch_client, autospec=True) as mock_client:
                mock_client.send = MagicMock(
                    AsyncMock(side_effect=handle_client_msg)
                )
                self.vsc = VanillaSimController(
                    "test",
                    "test2",
                    [1, 2],
                    [3],
                    agent_dic,
                    [
                        {
                            "name": (
                                "palaestrai.simulation:"
                                "VanillaSimControllerTerminationCondition"
                            ),
                            "params": {},
                        }
                    ],
                    mode="train",
                )

    async def test_term_condition_true(self):
        self.vsc.conductor_shutdown = AsyncMock(return_value=None)
        self.vsc.agent_shutdown = AsyncMock(return_value=None)
        self.vsc.env_shutdown = AsyncMock(return_value=None)

        msg = SimulationControllerTerminationResponse(
            "0", "1", "2", False, False
        )
        self.vsc.run_gov_client.send = AsyncMock(return_value=msg)

        await self.vsc.simulation_shutdown(True, [1], None)
        self.vsc.agent_shutdown.assert_called_once()
        self.vsc.env_shutdown.assert_called_once()

    async def test_term_condition_no_complete_shutdown(self):
        self.vsc.conductor_shutdown = MagicMock(return_value=None)
        self.vsc.agent_shutdown = AsyncMock(return_value=None)
        self.vsc.env_shutdown = AsyncMock(return_value=None)
        msg = SimulationControllerTerminationResponse(
            "0", "1", "2", False, False
        )
        self.vsc.run_gov_client.send = AsyncMock(return_value=msg)

        await self.vsc.simulation_shutdown(True, [1], None)
        self.vsc.conductor_shutdown.assert_not_called()

    def test_env_update(self):
        rsp_list = []
        sensor_list = []
        reward_list = []
        for i in range(4):
            sen = [SensorInformation(1, Discrete(1), i)]
            sensor_list.extend(sen)
            reward = RewardInformation(i * 2, Discrete(1), "Test")
            reward_list.append(reward)
            msg = EnvironmentUpdateResponse(
                sender_environment_id="0",
                receiver_simulation_controller_id="0",
                environment_conductor_id="0",
                experiment_run_id=str(i),
                sensors=sen,
                reward=[reward],
                is_terminal=True,
            )
            rsp_list.append(msg)

        sensors, rewards, termination = self.vsc.env_update(rsp_list)

        self.assertTrue(termination)
        self.assertListEqual(rewards, reward_list)
        self.assertListEqual(sensors, sensor_list)

    def test_agent_update(self):
        rsp_list = []
        actuator_list = []
        for i in range(4):
            actuator = [ActuatorInformation(i, Discrete(1), i)]
            actuator_list.extend(actuator)
            msg = AgentUpdateResponse(
                sender_agent_id="a",
                receiver_simulation_controller_id="s",
                actuator_information=actuator,
                sensor_information=[],
                experiment_run_id=str(i),
            )
            rsp_list.append(msg)

        actuators = self.vsc.agent_update(rsp_list)

        self.assertListEqual(actuators, actuator_list)

    async def test_simulation_stop_at_termination(self):
        reward = [RewardInformation(0.0, Discrete(1), "Test")]
        self.vsc.termination_condition = (
            VanillaSimControllerTerminationCondition()
        )
        self.vsc.env_ids = [0]
        self.vsc.get_env_update = AsyncMock(
            return_value=EnvironmentUpdateResponse(
                sender_environment_id="0",
                receiver_simulation_controller_id="0",
                environment_conductor_id="0",
                experiment_run_id="0",
                sensors=[SensorInformation(1, Discrete(1), 0)],
                reward=reward,
                is_terminal=True,
            )
        )
        self.vsc.get_agent_update = AsyncMock(
            return_value=AgentUpdateResponse(
                sender_agent_id="a",
                receiver_simulation_controller_id="s",
                actuator_information=[],
                sensor_information=[],
                experiment_run_id=str("e"),
            )
        )
        self.vsc.simulation_shutdown = MagicMock(AsyncMock(return_value=None))
        self.vsc.continue_simulation = AsyncMock(return_value=False)

        await self.vsc.simulation()
        self.vsc.continue_simulation.assert_called_once_with(
            True, reward, None
        )

    async def test_continue_simulation_no_termination(self):
        self.vsc.ex_termination = False
        result = await self.vsc.continue_simulation(False, 0, dict())

        self.assertTrue(result)

    async def test_continue_simulation_ex_termination(self):
        self.vsc.ex_termination = True
        self.vsc.stop_simulation = AsyncMock()

        result = await self.vsc.continue_simulation(False, 0, dict())

        self.assertFalse(result)

    async def test_continue_simulation_restart(self):
        self.vsc.ex_termination = False
        self.vsc.send_termination_request = AsyncMock(
            return_value=SimulationControllerTerminationResponse(
                "0", "1", "2", True, False
            )
        )
        self.vsc.stop_simulation = AsyncMock()

        result = await self.vsc.continue_simulation(True, 0, dict())

        self.assertTrue(result)

    async def test_continue_simulation_termination(self):
        self.vsc.ex_termination = False
        self.vsc.send_termination_request = AsyncMock(
            return_value=SimulationControllerTerminationResponse(
                "0", "1", "2", True, True
            )
        )
        self.vsc.stop_simulation = AsyncMock()

        result = await self.vsc.continue_simulation(True, 0, dict())

        self.assertFalse(result)

    def test_access_list(self):
        wanted_sensors = ["test-1", "test-2", "test-3"]
        wanted_actuators = ["test-4", "test-5", "test-6"]

        self.vsc.all_actuators = []
        self.vsc.all_actuators = []
        self.assertEqual(
            self.vsc.access_list(wanted_sensors, wanted_actuators), ([], [])
        )

        self.vsc.all_sensors = [
            SensorInformation(0, Discrete(1), "test-1"),
            SensorInformation(0, Discrete(1), "test-4"),
        ]
        self.vsc.all_actuators = []
        self.assertEqual(
            self.vsc.access_list(wanted_sensors, wanted_actuators),
            ([self.vsc.all_sensors[0]], []),
        )

        self.vsc.all_actuators = [
            ActuatorInformation(
                Box(0, 1, shape=(1,)), Discrete(1), "test-1337"
            ),
            ActuatorInformation(Box(0, 1, shape=(1,)), Discrete(1), "test-5"),
        ]
        self.assertEqual(
            self.vsc.access_list(wanted_sensors, wanted_actuators),
            ([self.vsc.all_sensors[0]], [self.vsc.all_actuators[1]]),
        )


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()
