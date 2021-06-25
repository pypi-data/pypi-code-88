from ..base import *
from ..models import *
from .mixins import *


class TaskResource(GetResourceMixin, BaseResource):
    def __init__(self, parent: BaseResource):
        super().__init__("tasks", Task, parent.client)
        self.parent = parent

    def construct(self, response):
        return Task(response, api_resource=self)

Mapping.register(Task, TaskResource)