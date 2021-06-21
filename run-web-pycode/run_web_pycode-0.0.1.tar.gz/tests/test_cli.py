#!/usr/bin/env python
# encoding: utf-8

from fire import testutils

from run_web_pycode import __main__


class CoreTest(testutils.BaseTestCase):
    def test_version(self):
        with self.assertOutputMatches(stdout=".*"):
            __main__.fire.Fire(__main__.version, command=[])

    def test_version_help_info(self):
        with self.assertRaisesFireExit(0, regexp="show version"):
            __main__.fire.Fire(
                {"version": __main__.version}, command=["version", "--help"]
            )

    def test_run(self):
        with self.assertOutputMatches(stdout="is a python script"):
            code_url = "https://raw.githubusercontent.com/AngusWG/run-web-pycode/master/tests/a_script.py"
            __main__.fire.Fire(
                {"run": __main__.run_remote_script}, command=["run", code_url]
            )
