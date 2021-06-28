import json
import os
import unittest

from worker.mixins.rollbar import payload_handler
from worker.test.utils import file_to_json


class TestRollbarPayloadHandler(unittest.TestCase):
    def test_rollbar_payload_handler(self):
        original_payload = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'resources', 'test', 'original_rollbar_payload.json')
        )
        original_payload = file_to_json(original_payload)
        self.assertEqual(
            len(json.dumps(original_payload["data"]["body"]["trace"]["frames"][1]["locals"]["dataset"])), 12903
        )

        trimmed_payload = payload_handler(original_payload)

        # After trimming, the local becomes a string with reduced number of characters
        self.assertEqual(len(trimmed_payload["data"]["body"]["trace"]["frames"][1]["locals"]["dataset"]), 1127)
