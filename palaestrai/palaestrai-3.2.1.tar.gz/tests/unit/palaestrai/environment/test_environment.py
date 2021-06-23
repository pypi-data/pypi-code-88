import unittest
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

from palaestrai.agent import SensorInformation, ActuatorInformation
from palaestrai.core.protocol import (
    EnvironmentShutdownRequest,
    EnvironmentShutdownResponse,
    EnvironmentStartRequest,
    EnvironmentStartResponse,
    EnvironmentUpdateRequest,
    EnvironmentUpdateResponse,
    EnvironmentResetRequest,
    EnvironmentResetResponse,
)
from palaestrai.environment.dummy_environment import DummyEnvironment
from palaestrai.environment.dummy_reward import DummyReward
from palaestrai.types import Discrete


def check_identifier(information, identifier="testenv"):
    for i in information:
        if identifier not in i.id:
            print(i.id)
            return False
    return True


class TestEnvironment(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.env = DummyEnvironment(
            "test_conn", uuid4(), DummyReward(), 123, {"identifier": "testenv"}
        )
        self.setup_req = EnvironmentStartRequest(
            environment_id="0",
            run_id="1",
        )
        self.update_req = EnvironmentUpdateRequest(
            sender_simulation_controller="2",
            receiver_environment="0",
            experiment_run_id="1",
            environment_conductor_id="3",
            actuators=list(),
        )
        self.shutdown_req = EnvironmentShutdownRequest(
            experiment_run_id="1", environment_id="0"
        )
        self.reset_req = EnvironmentResetRequest("0", "1")
        # self.reset_rsp = EnvironmentResetResponse("0")

    def test_handle_setup(self):
        self.env.start_environment = MagicMock(
            return_value=(
                [SensorInformation(0, Discrete(1), "0")],
                [ActuatorInformation(0, Discrete(1), "0")],
            )
        )
        rsp = self.env._handle_setup(self.setup_req)

        self.env.start_environment.assert_called_once()
        self.assertIsInstance(rsp, EnvironmentStartResponse)
        self.assertTrue(check_identifier(rsp.sensors))
        self.assertTrue(check_identifier(rsp.actuators))

    def test_handle_update(self):
        self.env.update = MagicMock(
            return_value=([SensorInformation(0, Discrete(1), "0")], False)
        )
        rsp = self.env._handle_update(self.update_req)

        self.env.update.assert_called_once()
        self.assertIsInstance(rsp, EnvironmentUpdateResponse)
        self.assertTrue(check_identifier(rsp.sensors))

    def test_handle_shutdown(self):
        self.env.shutdown = MagicMock(return_value=True)
        rsp = self.env._handle_shutdown(self.shutdown_req)

        self.env.shutdown.assert_called_once()
        self.assertIsInstance(rsp, EnvironmentShutdownResponse)

    def test_handle_reset(self):
        self.env.shutdown = MagicMock()
        self.env.start_environment = MagicMock(
            return_value=(
                [SensorInformation(0, Discrete(1), "0")],
                [ActuatorInformation(0, Discrete(1), "0")],
            )
        )
        result = self.env._handle_reset(self.reset_req)

        self.assertIsInstance(result, EnvironmentResetResponse)
        self.assertTrue(check_identifier(result.sensors))
        self.assertTrue(check_identifier(result.actuators))

        self.env.shutdown.assert_called_once()
        self.env.start_environment.assert_called_once()

    async def test_run(self):
        setup_msg = self.setup_req
        update_msg = self.update_req
        shutdown_msg = self.shutdown_req
        self.env.worker.transceive = AsyncMock()
        self.env.worker.transceive.side_effect = [
            setup_msg,
            update_msg,
            update_msg,
            update_msg,
            shutdown_msg,
            shutdown_msg,  # Final message, will not be handled
        ]
        self.env.start_environment = MagicMock(return_value=(list(), list()))
        self.env.update = MagicMock(return_value=(list(), False))
        await self.env.run()

        self.assertEqual(self.env.worker.transceive.call_count, 6)
        self.env.start_environment.assert_called_once()
        self.assertEqual(self.env.update.call_count, 3)


if __name__ == "__main__":
    unittest.main()
