import unittest
from ep2_core.common import *


class TestFileInformation(unittest.TestCase):

    def test_simple(self):
        f_info = FileInformation('Test')
        f_info.add_file('hello_world.txt', Action.ADD)

        self.assertEqual(f_info.info_string(),
"""Change list [Test]
\t+ hello_world.txt""", "Unexpected file info output")

    def test_all_actions(self):
        f_info = FileInformation('Test')
        f_info.add_file('hello_world.txt', Action.ADD)
        f_info.add_file('README.txt', Action.MODIFY)
        f_info.add_file('hello_all.txt', Action.DELETE)

        self.assertEqual(f_info.info_string(),
"""Change list [Test]
\t+ hello_world.txt
\t~ README.txt
\t- hello_all.txt""", "Unexpected file info output")

    def test_multiple_per_action(self):
        f_info = FileInformation('Test')
        f_info.add_file('hello_world1.txt', Action.ADD)
        f_info.add_file('hello_world2.txt', Action.ADD)
        f_info.add_file('hello_world3.txt', Action.ADD)
        f_info.add_file('README.txt', Action.MODIFY)
        f_info.add_file('hello_all.txt', Action.DELETE)

        self.assertEqual(f_info.info_string(),
"""Change list [Test]
\t+ hello_world1.txt
\t+ hello_world2.txt
\t+ hello_world3.txt
\t~ README.txt
\t- hello_all.txt""", "Unexpected file info output")

    def test_file_multiple_actions(self):
        f_info = FileInformation('Test')
        f_info.add_file('hello_world.txt', Action.ADD)
        f_info.add_file('README.txt', Action.MODIFY)
        f_info.add_file('hello_world.txt', Action.DELETE)
        f_info.add_file('hello_all.txt', Action.DELETE)

        self.assertEqual(f_info.info_string(),
"""Change list [Test]
\t~ README.txt
\t- hello_all.txt
\t- hello_world.txt""", "Unexpected file info output")

    def test_push(self):
        f_info = FileInformation('Test')
        f_info.add_file('hello_world.txt', Action.ADD, True)
        f_info.add_file('README.txt', Action.MODIFY, True)
        f_info.add_file('hello_all.txt', Action.DELETE)

        self.assertEqual(f_info.info_string(),
"""Change list [Test]
\t+ hello_world.txt*
\t~ README.txt*
\t- hello_all.txt
*commit and push changes""", "Unexpected file info output")

    def test_add_delete(self):
        f_info = FileInformation('Test')
        f_info.add_file('hello_world.txt', Action.ADD, True)
        f_info.add_file('README.txt', Action.MODIFY, True)
        f_info.add_file('hello_all.txt', Action.DELETE)
        f_info.delete('hello_world.txt', True)

        self.assertEqual(f_info.info_string(),
"""Change list [Test]
\t~ README.txt*
\t- hello_all.txt
*commit and push changes""", "Unexpected file info output")
