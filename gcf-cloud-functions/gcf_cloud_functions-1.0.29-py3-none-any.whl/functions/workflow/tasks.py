from abc import ABC

from gcf.functions.execution.config import ExecutionStatus
from gcf.functions.execution.worker import WorkflowWorker
from gcf.functions.workflow.events import TaskStatusUpdateEvent


class WorkflowTask(WorkflowWorker, ABC):

    def set_status(self, status: ExecutionStatus):
        # Call super
        WorkflowWorker.set_status(self, status)

        # Set status of current tasks on dispatcher
        # This is only for UI purposes
        dispatch_ref = self.doc_ref.parent.parent
        dispatch_ref.set({
            'current_task': {
                'status': status,
                'name': self.get_task_name()
            },
            'tasks': {
                self.task_name: {
                    'status': status
                }
            }
        }, merge=True)

        # Notify dispatcher that the work is done
        _, self.generated_event = dispatch_ref.collection('events').add(
            TaskStatusUpdateEvent(
                task_name=self.get_task_name(),
                task_status=status
            ).to_dict())
