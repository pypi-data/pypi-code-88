import itertools
import json
from typing import Dict, Union
from worker.data.api import API

from worker import App
from worker.event import Event, EventType
from worker.event.scheduled import SingleScheduledEvent, ScheduledEvent
from worker.event.stream import StreamEvent
from worker.exceptions import EventFormatError
from worker.framework import constants


api = API()


class EventHandler:
    def __init__(self, app: App):
        self.app: App = app
        self.event_type: EventType = None
        self.event_by_asset_id: Dict[int, Event] = None

    def process(self, event: Union[str, dict]):
        """
        The whole process that is performed on an event including the
        loading, handling state, running, and completing the event.

        Args:
            event (Union[str, dict]): lambda handler event
        """
        self._load(event)
        self._run()

    def _load(self, event: Union[str, dict]):
        """
        Cleaning the event and group events based on their asset ids

        Args:
            event (Union[str, dict]): lambda handler event
        """
        self.event_type = self.get_event_type()
        event = self.clean_event(event)
        self.event_by_asset_id = self.format_event(self.event_type, event)

    def _run(self):
        """ Full run of the events based on their asset id """
        for asset_id, event in self.event_by_asset_id.items():
            self.app.load(self.event_type, event)
            self.app.run_modules()
            self.app.save_state()
            event.complete_event(api)

    @staticmethod
    def get_event_type() -> EventType:
        event_type: str = constants.get('global.event-type', "")
        return EventType(event_type)

    @staticmethod
    def clean_event(event):
        if not event:
            raise Exception("Empty event")

        if isinstance(event, (str, bytes, bytearray)):
            event = json.loads(event)

        return event

    @staticmethod
    def format_event(event_type: EventType, event: list) -> dict:
        """
        validate the wits_stream event, flatten and organize the data into a desired format
        :param event_type: type of event
        :param event: the wits or scheduler json event
        :return: a dict of records that are grouped by the asset_ids
        """
        if event_type == EventType.SCHEDULER:
            if not isinstance(event[0], list):
                raise EventFormatError("Invalid event!")

            # Scheduler events type is 'list of lists'; flattening into a single list
            events = [SingleScheduledEvent(item) for sublist in event for item in sublist]
            merging_function = ScheduledEvent

        else:  # 'wits_stream'
            events = [StreamEvent(each) for each in event]
            merging_function = StreamEvent.merge

        # sorting is required otherwise we only capture the last group of each asset_id
        events.sort(key=lambda single_event: single_event.asset_id)
        groups = itertools.groupby(events, key=lambda single_event: single_event.asset_id)

        events_by_asset_id = {
            group: merging_function(list(dataset))
            for group, dataset in groups
        }

        return events_by_asset_id
