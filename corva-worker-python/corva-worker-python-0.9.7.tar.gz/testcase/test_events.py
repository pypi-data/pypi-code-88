import copy
import os
import unittest
from worker.event.event_handler import EventHandler
from worker.test.utils import file_to_json

from worker.framework import constants


default_parameters = copy.deepcopy(constants.parameters)


class TestEvents(unittest.TestCase):
    def _load_event(self, filename: str) -> dict:
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "test", "events", filename)
        )
        event = file_to_json(file_path)
        return event

    def test_stream_events(self):
        constants.update({
            "global": {
                "event-type": "wits_stream",
                "post-to-message-producer": True,
            }
        })

        wits_stream = self._load_event("wits_stream.json")

        event_handler = EventHandler(app=None)
        event_handler._load(wits_stream)

        expected_output = {
            # asset_id: length of events
            265: 22,
            1000: 6
        }

        self.assertTrue(event_handler.event_by_asset_id[265].is_posting_to_message_producer)

        for asset_id, stream in event_handler.event_by_asset_id.items():
            self.assertEqual(expected_output[asset_id], len(stream))

        constants.parameters = copy.deepcopy(default_parameters)

    def test_scheduled_events(self):
        constants.update({"global": {"event-type": "scheduler"}})

        scheduler = self._load_event("scheduler.json")

        event_handler = EventHandler(app=None)
        event_handler._load(scheduler)

        expected_output = {
            # asset_id: length of events
            1: 9,
            2: 2,
            3: 1
        }

        for asset_id, records in event_handler.event_by_asset_id.items():
            self.assertEqual(expected_output[asset_id], len(records))

        constants.parameters = copy.deepcopy(default_parameters)
