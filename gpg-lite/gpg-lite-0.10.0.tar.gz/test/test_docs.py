import os
import unittest
from pathlib import Path

WITH_GPG = os.environ.get("WITH_GPG", None) == "true"


@unittest.skipUnless(WITH_GPG, "Integration tests")
class TestDocs(unittest.TestCase):
    @staticmethod
    def test_gen_key():
        """Read the python code snippets from README and exec"""
        read = False
        code = ""
        with open(Path(__file__).parent.parent / "README.md", encoding="utf-8") as doc:
            for line in doc:
                if line == "```python\n":
                    read = True
                    continue
                if line == "```\n":
                    read = False
                    continue
                if read:
                    code += line

        exec(code)  # pylint: disable=exec-used
