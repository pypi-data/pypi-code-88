"""
This module contains the class :class:`DummyEnvironment`. It could be
used in an experiment for reference purposes.
"""
import random
from typing import List

from palaestrai.agent import SensorInformation, ActuatorInformation
from palaestrai.types import Discrete
from .environment import Environment
from ..agent.reward_information import RewardInformation


class DummyEnvironment(Environment):
    """
    This class provides a dummy environment with a fixed number of sensors. The
    environment terminates after a fixed number of updates.

    Parameters
    ----------
    connection : broker_connection
        the URI which is used to connect to the simulation broker. It is used
        to communicate with the simulation controller.
    uid : uuid4
        a universal id for the environment
    seed : int
        Seed for recreation
    params : dict
        parameters which are necessary for the environment execution
        default to None
    """

    def calc_reward(
        self,
        sensors: List[SensorInformation],
        actuators: List[ActuatorInformation],
    ) -> List[RewardInformation]:
        return [RewardInformation(0, Discrete(2), "Reward")]

    def __init__(self, connection, uid, reward, seed: int, params=None):
        super().__init__(connection, uid, reward, seed, params)
        self.iter: int

    def start_environment(self):
        """
        This method is called when an `EnvironmentStartRequest` message is
        received. This dummy environment is represented by 10 sensors and
        10 actuators. The sensors are of the type `SensorInformation` and have
        a random value of either 0 or 1, an `observation_space` between 0 and 1
        and an integer number as id.
        The actuators are of the type `ActuatorInformation` and contain a
        setpoint of Discrete(1), an `action_space` of None and an integer
        number as id.

        Returns
        -------
        tuple :
            A list containing the `SensorInformation` for each of the 10
            sensors and a list containing the `ActuatorInformation` for each
            of the 10 actuators.
        """
        self.iter = 0
        sensors = []
        for num in range(10):
            sensors.append(self._create_sensor(num))
            actuator = ActuatorInformation(
                action_space=Discrete(2), setpoint=None, actuator_id=num
            )
            self.actuators.append(actuator)
        return sensors, self.actuators

    def update(self, actuators):
        """
        This method is called when an `EnvironmentUpdateRequest` message is
        received. While setpoints of the actuators manipulate an actual
        environment, in here those setpoints have no impact on the behavior of
        the dummy environment.
        The state of this dummy environment is represented via random values of
        the `SensorInformation` from the 10 sensors.
        In this dummy environment the reward for the state is a random value of
        either 0 or 1.
        The method returns a list of `SensorInformation`, the random reward and
        the boolean `is_terminal`. After 10 updates the `is_terminal` value is
        set to True which triggers the respective shutdown messages.

        Parameters
        ----------
        actuators : list[`ActuatorInformation`]
            A list of `ActuatorInformation` to interact with the environment.

        Returns
        -------
        tuple :
            A list of `SensorInformation` representing the 10 sensors, the
            random reward and boolean for `is_terminal`.

        """
        if self.iter < 10:
            self.iter += 1
            sensors = []
            for num in range(10):
                sensors.append(self._create_sensor(num))
            return sensors, False
        else:
            return list(), True

    def _create_sensor(self, sensor_id):
        return SensorInformation(
            sensor_value=random.randint(0, 1),
            observation_space=Discrete(2),
            sensor_id=sensor_id,
        )
