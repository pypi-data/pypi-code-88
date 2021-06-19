# -*- coding: utf-8 -*-
"""Dispatch Service.

The dispatcher will invoke the next task as defined in the workflow, the `DispatchService`
must be subclassed by a concrete implementation providing the steps.

The dispatcher will execute when a document is created in the firestore ``events`` collection and it will:
    - read event's `service_name` and `service_status`
    - if `service_status` is `done`
        - create a document in the ``jobs`` collection representing the next step.
        - create a document in the new job's firestore ``event`` collection.

Example:
       >>> class GithubDispatchService(DispatchService):
       ...
       ...      def get_workflow(self) -> List[str]:
       ...          return ['ingest', 'transform', 'summary']
"""


from typing import List
from abc import abstractmethod, ABC

from google.cloud.firestore_v1 import DocumentReference

from gcf.functions.execution.config import ExecutionStatus
from gcf.functions.execution.worker import WorkflowWorker
from gcf.functions.workflow.events import TaskStartEvent


class DispatchTask(WorkflowWorker, ABC):

    def get_task_name(self) -> str:
        return 'dispatch'

    @abstractmethod
    def get_workflow(self) -> List[str]:
        """
        Abstract method that must return the list of tasks that this workflow has.

        Returns:
            list of steps as string.
        """

        raise NotImplementedError

    def on_task_update(self, task_name: str, task_status: ExecutionStatus):
        """
        Hook for signaling a task update.

        Args:
            task_name: The task's name.
            task_status: The task's execution status.
        """

        pass

    def on_trigger_next_task(self, task_name: str, event_path: str):
        pass

    def _get_next_task(self, current_task):
        tasks = self.get_workflow()

        # TODO: review this
        if current_task is None or current_task == 'dispatch':
            return tasks[0]

        current_step_index = tasks.index(current_task)
        if current_step_index < len(tasks) - 1:
            return tasks[current_step_index + 1]

        return None

    def _trigger_next_task(self, next_task):
        state_ref = self.event.event_ref.parent.parent

        next_task_ref = state_ref.collection('tasks').document(next_task)
        next_task_ref.set({})

        _, self.generated_event = next_task_ref.collection('events').add(TaskStartEvent(task_name=next_task).to_dict())
        self.on_trigger_next_task(next_task, self.generated_event.path)

    def work(self):
        current_task = self.event.context.task_name
        next_task = self._get_next_task(current_task)

        current_task_status = self.event.context.task_status or ExecutionStatus.SUCCESS

        doc_ref = self.event.event_ref.parent.parent
        doc_ref.update({
            'active': True,
            'workflow': self.get_workflow()
        })

        if current_task:
            doc_ref.set({
                'tasks': {
                    current_task: {
                        'status': current_task_status
                    }
                }
            }, merge=True)

        if next_task:
            if current_task_status == ExecutionStatus.SUCCESS:
                self._trigger_next_task(next_task)
            else:
                doc_ref.update({'active': False})
        else:
            doc_ref.update({'active': False})

        self.on_task_update(task_name=current_task, task_status=current_task_status)
