import unittest
import os
from collections import namedtuple
from unittest.mock import patch, mock_open
import re
from .apps import app_command_factory
from .apps_utils import APPS_PATH


def find(calls, word: str):
    for call in calls:
        call_args, kwargs = call
        if any([arg.find(word) >= 0 for arg in call_args]):
            return True
    return False


args = namedtuple("args", ["info", "reset", "delete", "config", "public"])


class AppsCommand(unittest.TestCase):
    @patch("builtins.print", autospec=True, side_effect=print)
    @patch("builtins.open", new_callable=mock_open,
           read_data='{"app1":{"dir":"/home/app1","status":"local"}}')
    def test_info_show_apps(self, mock_file, mock_print):
        app_command_factory(args(info=True, reset=False, delete=False, config=False, public=False)).run()
        calls = mock_print.call_args_list
        self.assertTrue(find(calls,"app1"))
        self.assertTrue(find(calls,"/home/app1"))
        self.assertTrue(find(calls,"local"))
        mock_file.assert_called_with(APPS_PATH, 'r')

    @patch("builtins.print", autospec=True, side_effect=print)
    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_info_show_no_apps(self, mock_file, mock_print):
        app_command_factory(args(info=True, reset=False, delete=False, config=False, public=False)).run()
        calls = mock_print.call_args_list
        # print("Beyrem:",calls)
        self.assertTrue(find(calls, "No apps to display"))
        mock_file.assert_called_with(APPS_PATH, 'r')


if __name__ == '__main__':
    unittest.main()
