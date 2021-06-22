# Created by Jan Rummens at 22/06/2021
import unittest
from nemonet.runner.vision_runner import Runner

class MyTestCase(unittest.TestCase):
    def test_chrome_options(self):
        runner = Runner(runner_config="runner_config.json")
        runner.execute_scenario("command-right-mouse")


if __name__ == '__main__':
    unittest.main()
