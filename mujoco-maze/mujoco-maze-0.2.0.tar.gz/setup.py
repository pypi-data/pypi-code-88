# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mujoco_maze']

package_data = \
{'': ['*'], 'mujoco_maze': ['assets/*']}

install_requires = \
['gym>=0.16', 'mujoco-py>=1.5']

entry_points = \
{'console_scripts': ['test = pytest:main']}

setup_kwargs = {
    'name': 'mujoco-maze',
    'version': '0.2.0',
    'description': 'Simple maze environments using mujoco-py',
    'long_description': '# mujoco-maze\n[![Actions Status](https://github.com/kngwyu/mujoco-maze/workflows/CI/badge.svg)](https://github.com/kngwyu/mujoco-maze/actions)\n[![PyPI version](https://img.shields.io/pypi/v/mujoco-maze?style=flat-square)](https://pypi.org/project/mujoco-maze/)\n[![Black](https://img.shields.io/badge/code%20style-black-000.svg)](https://github.com/psf/black)\n\nSome maze environments for reinforcement learning (RL) based on [mujoco-py]\nand [openai gym][gym].\n\nThankfully, this project is based on the code from  [rllab] and\n[tensorflow/models][models].\n\nNote that [d4rl] and [dm_control] have similar maze\nenvironments, and you can also check them.\nBut, if you want more customizable or minimal one, I recommend this.\n\n## Usage\n\nImporting `mujoco_maze` registers environments and you can load\nenvironments by `gym.make`.\nAll available environments listed are listed in [Environments] section.\n\nE.g.,:\n```python\nimport gym\nimport mujoco_maze  # noqa\nenv = gym.make("Ant4Rooms-v0")\n```\n\n## Environments\n\n- PointUMaze/AntUmaze/SwimmerUmaze\n\n  ![PointUMaze](./screenshots/PointUMaze.png)\n  - PointUMaze-v0/AntUMaze-v0/SwimmerUMaze-v0 (Distance-based Reward)\n  - PointUmaze-v1/AntUMaze-v1/SwimmerUMaze-v (Goal-based Reward i.e., 1.0 or -ε)\n\n- PointSquareRoom/AntSquareRoom/SwimmerSquareRoom\n\n  ![SwimmerSquareRoom](./screenshots/SwimmerSquareRoom.png)\n  - PointSquareRoom-v0/AntSquareRoom-v0/SwimmerSquareRoom-v0 (Distance-based Reward)\n  - PointSquareRoom-v1/AntSquareRoom-v1/SwimmerSquareRoom-v1 (Goal-based Reward)\n  - PointSquareRoom-v2/AntSquareRoom-v2/SwimmerSquareRoom-v2 (No Reward)\n\n- Point4Rooms/Ant4Rooms/Swimmer4Rooms\n\n  ![Point4Rooms](./screenshots/Point4Rooms.png)\n  - Point4Rooms-v0/Ant4Rooms-v0/Swimmer4Rooms-v0 (Distance-based Reward)\n  - Point4Rooms-v1/Ant4Rooms-v1/Swimmer4Rooms-v1 (Goal-based Reward)\n  - Point4Rooms-v2/Ant4Rooms-v2/Swimmer4Rooms-v2 (Multiple Goals (0.5 pt or 1.0 pt))\n\n- PointCorridor/AntCorridor/SwimmerCorridor\n\n  ![PointCorridor](./screenshots/PointCorridor.png)\n  - PointCorridor-v0/AntCorridor-v0/SwimmerCorridor-v0 (Distance-based Reward)\n  - PointCorridor-v1/AntCorridor-v1/SwimmerCorridor-v1 (Goal-based Reward)\n  - PointCorridor-v2/AntCorridor-v2/SwimmerCorridor-v2 (No Reward)\n\n- PointPush/AntPush\n\n  ![PointPush](./screenshots/AntPush.png)\n  - PointPush-v0/AntPush-v0 (Distance-based Reward)\n  - PointPush-v1/AntPush-v1 (Goal-based Reward)\n\n- PointFall/AntFall\n\n  ![PointFall](./screenshots/AntFall.png)\n  - PointFall-v0/AntFall-v0 (Distance-based Reward)\n  - PointFall-v1/AntFall-v1 (Goal-based Reward)\n\n- PointBilliard\n\n  ![PointBilliard](./screenshots/PointBilliard.png)\n  - PointBilliard-v0 (Distance-based Reward)\n  - PointBilliard-v1 (Goal-based Reward)\n  - PointBilliard-v2 (Multiple Goals (0.5 pt or 1.0 pt))\n  - PointBilliard-v3 (Two goals (0.5 pt or 1.0 pt))\n  - PointBilliard-v4 (No Reward)\n\n## Customize Environments\nYou can define your own task by using components in `maze_task.py`,\nlike:\n\n```python\nimport gym\nimport numpy as np\nfrom mujoco_maze.maze_env_utils import MazeCell\nfrom mujoco_maze.maze_task import MazeGoal, MazeTask\nfrom mujoco_maze.point import PointEnv\n\n\nclass GoalRewardEMaze(MazeTask):\n    REWARD_THRESHOLD: float = 0.9\n    PENALTY: float = -0.0001\n\n    def __init__(self, scale):\n        super().__init__(scale)\n        self.goals = [MazeGoal(np.array([0.0, 4.0]) * scale)]\n\n    def reward(self, obs):\n        return 1.0 if self.termination(obs) else self.PENALTY\n\n    @staticmethod\n    def create_maze():\n        E, B, R = MazeCell.EMPTY, MazeCell.BLOCK, MazeCell.ROBOT\n        return [\n            [B, B, B, B, B],\n            [B, R, E, E, B],\n            [B, B, B, E, B],\n            [B, E, E, E, B],\n            [B, B, B, E, B],\n            [B, E, E, E, B],\n            [B, B, B, B, B],\n        ]\n\n\ngym.envs.register(\n    id="PointEMaze-v0",\n    entry_point="mujoco_maze.maze_env:MazeEnv",\n    kwargs=dict(\n        model_cls=PointEnv,\n        maze_task=GoalRewardEMaze,\n        maze_size_scaling=GoalRewardEMaze.MAZE_SIZE_SCALING.point,\n        inner_reward_scaling=GoalRewardEMaze.INNER_REWARD_SCALING,\n    )\n)\n```\nYou can also customize models. See `point.py` or so.\n\n## Warning\nReacher enviroments are not tested.\n\n## [Experimental] Web-based visualizer\nBy passing a port like `gym.make("PointEMaze-v0", websock_port=7777)`,\none can use a web-based visualizer when calling `env.render()`.\n![WebBasedVis](./screenshots/WebVis.png)\n\nThis feature is experimental and can produce some zombie proceses.\n\n## License\nThis project is licensed under Apache License, Version 2.0\n([LICENSE](LICENSE) or http://www.apache.org/licenses/LICENSE-2.0).\n\n[d4rl]: https://github.com/rail-berkeley/d4rl\n[dm_control]: https://github.com/deepmind/dm_control\n[gym]: https://github.com/openai/gym\n[models]: https://github.com/tensorflow/models/tree/master/research/efficient-hrl\n[mujoco-py]: https://github.com/openai/mujoco-py\n[rllab]: https://github.com/rll/rllab\n',
    'author': 'Yuji Kanagawa',
    'author_email': 'yuji.kngw.80s.revive@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kngwyu/mujoco-maze',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
