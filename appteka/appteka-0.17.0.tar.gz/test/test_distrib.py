import unittest
from appteka.distrib import micro_version, minor_version, major_version
from appteka.distrib import build_folder_name


class Test_build_folder_name(unittest.TestCase):
    def test_no_appendix(self):
        name = build_folder_name("NAME", "0.2.1")
        self.assertIn("build/NAME-0.2.1-", name)
        self.assertEqual(name[-3:], "bit")

    def test_with_appendix(self):
        name = build_folder_name("NAME", "0.2.1", "appendix")
        self.assertIn("build/NAME-0.2.1-appendix-", name)
        self.assertEqual(name[-3:], "bit")

    def test_with_empty(self):
        name = build_folder_name("NAME", "0.2.1", "")
        self.assertNotIn("build/NAME-0.2.1--", name)
        self.assertEqual(name[-3:], "bit")


class Test_mirco_version(unittest.TestCase):
    def test_regular_case(self):
        ver = "0.2.11"
        self.assertEqual(micro_version(ver), 11)

    def test_2_parts_so_zero_micro(self):
        ver = "0.2"
        self.assertEqual(micro_version(ver), 0)

    def test_4_parts(self):
        ver = "0.2.1.3"
        self.assertEqual(micro_version(ver), 1)


class Test_minor_version(unittest.TestCase):
    def test_regular_case(self):
        ver = "0.2.11"
        self.assertEqual(minor_version(ver), 2)

    def test_1_part(self):
        ver = "15"
        self.assertEqual(minor_version(ver), 0)

    def test_2_part(self):
        ver = "0.2"
        self.assertEqual(minor_version(ver), 2)

    def test_4_parts(self):
        ver = "0.2.1.3"
        self.assertEqual(minor_version(ver), 2)


class Test_major_version(unittest.TestCase):
    def test_regular_case(self):
        ver = "0.2.11"
        self.assertEqual(major_version(ver), 0)
