from typing import List, TypeVar, Union

from ..models.base import BaseModel
from ..models.execution import Execution
from ..models.mixins import DeleteModelMixin, ParentMixin, SaveModelMixin
from ..models.task import Task
from ..resources.task_resource import TaskResource

T = TypeVar("T")


class Workflow(ParentMixin, SaveModelMixin, DeleteModelMixin, BaseModel):
    def __init__(
        self,
        url=None,
        id=None,
        name=None,
        title=None,
        tasks=None,
        error_task=None,
        task_defaults=None,
        variables=None,
        usages=None,
        project=None,
        project_id=None,
        created_at=None,
        updated_at=None,
        last_execution=None,
        description=None,
        extra=None,
        labels=None,
        permissions=None,
        version=None,
        updated_by=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.url = url
        self.id = id
        self.name = name
        self.title = title
        self.tasks = tasks
        self.error_task = error_task
        self.task_defaults = task_defaults
        self.variables = variables
        self.usages = usages
        self.project = project
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_execution = last_execution
        self.description = description
        self.extra = extra
        self.labels = labels
        self.permissions = permissions
        self.version = version
        self.updated_by = updated_by

        self._read_only = [
            "url",
            "id",
            "usages",
            "project",
            "project_id",
            "created_at",
            "updated_at",
            "last_execution",
            "permissions",
            "version",
            "update_by",
        ]

    @property
    def _subresources(self):
        return {Task: TaskResource}

    def run(self, input=None) -> Execution:
        return self.api_resource.run(self, input=input)

    def duplicate(self: T, name=None, title=None) -> T:
        return self.api_resource.duplicate(self, name=name, title=title)

    def _tasks(self, identifier=None, **kwargs) -> Union[Task, List[Task]]:
        return self._get(Task, identifier, **kwargs)
