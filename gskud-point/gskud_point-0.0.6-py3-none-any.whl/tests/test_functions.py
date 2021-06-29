import unittest
from skud_point import functions
import datetime


class FunctionsTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_states = {'LOCKED': None}

    def test_set_last_state(self):
        state = 'LOCKED'
        timestamp = datetime.datetime.now()

        functions.update_last_state(self.last_states, state, timestamp)

        self.assertTrue(self.last_states[state] == timestamp)


if __name__ == '__main__':
    unittest.main()