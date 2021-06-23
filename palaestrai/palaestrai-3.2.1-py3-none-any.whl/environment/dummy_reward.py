from typing import List

from palaestrai.agent import SensorInformation, RewardInformation
from palaestrai.environment.reward import Reward
from palaestrai.types import Discrete


class DummyReward(Reward):
    def __call__(
        self, state: List[SensorInformation], *args, **kwargs
    ) -> List[RewardInformation]:
        reward = 0
        for sensor in state:
            reward += sensor()
        if reward < 9000:
            return [RewardInformation(reward, Discrete(9000), "Reward")]
        else:
            # This reward is over 9000, maybe add a log
            return [RewardInformation(9000, Discrete(9000), "Reward")]
