from firebase_admin import firestore
from google.cloud import firestore_v1
from google.cloud.firestore_v1 import DocumentReference

from gcf import __version__
from gcf.functions.execution.config import ExecutionStatus, EventType


class EventContext(object):

    def __init__(self, api_version: str, event_type: EventType, task_name: str, task_status: ExecutionStatus):
        self.api_version = api_version
        self.event_type = event_type
        self.task_name = task_name
        self.task_status = task_status

    def to_dict(self):
        return {
            'context': {
                'api_version': self.api_version,
                'event_type': self.event_type,
                'task_name': self.task_name,
                'task_status': self.task_status,
                'created_at': firestore.SERVER_TIMESTAMP
            }
        }

class Event(object):

    def __init__(self, event_data: dict, parent_data: dict, event_ref: DocumentReference):
        self.event_ref = event_ref
        self.id = event_ref.id

        self.event_data = event_data

        # TODO
        self.parent_data = parent_data
        self.parent_ref = event_ref.parent.parent

        event_context = event_data.get('context', {})
        self.context = EventContext(
            api_version=event_context.get('api_version', None),
            event_type=event_context.get('event_type', None),
            task_name=event_context.get('task_name', None),
            task_status=event_context.get('task_status', None)
        )

        self.allow_execution = False
        self.error = event_data.get('error', None)
        self.invocations = event_data.get('invocations', [])
        self.is_handled = event_data.get('handled', False)

    def to_dict(self):
        return {
            'handled': self.is_handled,
            'handling': {
                'api_version': __version__,
                'error': self.error,
            },
            'invocation_count': firestore_v1.transforms.Increment(1),
            'execution_count': firestore_v1.transforms.Increment(1 if self.allow_execution else 0),
            'invocations': self.invocations,
        }

    def add_invocation(self, invocation):
        self.invocations += [invocation]
