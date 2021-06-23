from ..models.base import BaseResource
from ..models.task import Task
from ..resources.mixins import GetResourceMixin


class TaskResource(GetResourceMixin, BaseResource):
    def __init__(self, parent:BaseResource):
        super().__init__("tasks", Task, parent.client)
        self.parent = parent

    def construct(self, response):
        return Task(response, api_resource=self)
