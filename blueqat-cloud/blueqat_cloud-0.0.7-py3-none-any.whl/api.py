"""Module for manage API"""
import json
from pathlib import Path
import re
import urllib.request
import typing
from typing import Any, List, Optional, Type, Union
import warnings

from .annealing import AnnealingTask, AnnealingResult
from .data import ExecutionRequest, ExecutionRequestEncoder, Status, TaskData, TaskListData
from .device import Device
from .task import CloudTask, CloudTaskOptions, TaskIter, TaskList
from .local import make_localtask, LocalTaskOptions

from .datafactory import make_executiondata, make_result

if typing.TYPE_CHECKING:
    from .task import AbstractTask
    from blueqat import Circuit

API_ENDPOINT = "https://cloudapi.blueqat.com/"


class Api:
    """Manage API and post request."""
    def __init__(self, api_key: str):
        self.api_key = api_key

    def post_request(
            self,
            path: str,
            body: Any,
            json_encoder: Optional[Type[json.JSONEncoder]] = None) -> Any:
        """Post request."""
        headers = {
            'Content-Type': 'application/json',
            'X-Api-Key': self.api_key,
        }
        req = urllib.request.Request(
            API_ENDPOINT + path,
            json.dumps(body, cls=json_encoder).encode(), headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return json.loads(body)

    def save_to_file(self, suffix: str = '') -> None:
        """Save API to file."""
        key_path = _get_apikey_path(suffix)
        parent_dir = key_path.parent
        parent_dir.mkdir(exist_ok=True)
        key_path.write_text(self.api_key)

    def save_api(self) -> None:
        """Save API to file."""
        warnings.warn("Api.save_api is deprecated. Use Api.save_to_file.",
                      DeprecationWarning)
        self.save_to_file()

    def credit(self) -> str:
        """Get credit."""
        path = "v1/credit/get"
        return self.post_request(path, {})["amount"]

    def status(self, taskid: str) -> Status:
        """Get task status."""
        path = "v2/quantum-tasks/get/status"
        res = self.post_request(path, {"id": taskid})
        return Status(res['status'])

    def post_executiondata(self, execdata: ExecutionRequest) -> 'AbstractTask':
        """Create new task"""
        path = "v2/quantum-tasks/create"
        res = self.post_request(path,
                                execdata,
                                json_encoder=ExecutionRequestEncoder)
        taskdata = TaskData.from_dict(res['task'])
        result = make_result(res.get('result', {}), Device(taskdata.device))
        return CloudTask(self, taskdata, result)

    def annealing(self, qubo: List[List[float]], chain_strength: int,
                  num_reads: int) -> AnnealingResult:
        """Create annealing task"""
        path = "v1/quantum-tasks/create"
        res = self.post_request(path, {
            "qubo": qubo,
            "chain_strength": chain_strength,
            "num_reads": num_reads
        })
        return AnnealingResult(res['task'])

    def execute(
        self,
        c: 'Circuit',
        device: Device,
        shots: int,
        options: Union[LocalTaskOptions, CloudTaskOptions, None] = None
    ) -> 'AbstractTask':
        """Create new task and execute the task."""
        if options is None:
            options = {}
        if device.value == 'local':
            return make_localtask(c, shots, options)
        execdata = make_executiondata(c, device, shots, options)
        return self.post_executiondata(execdata)

    def annealing_tasks(self, index: int = 0) -> List[AnnealingTask]:
        """Get tasks."""
        path = "v1/quantum-tasks/list"
        body = {
            "index": index,
        }
        tasks = self.post_request(path, body)
        assert isinstance(tasks, list)
        return [AnnealingTask(self, **task) for task in tasks]

    def task_result(self, task_id: str) -> CloudTask:
        """Get a task and result from task ID."""
        path = "v2/quantum-tasks/get"
        body = {
            "id": task_id,
        }
        task_result = self.post_request(path, body)
        taskdata = TaskData.from_dict(task_result['task'])
        result = make_result(task_result.get('result', {}),
                             Device(taskdata.device))
        return CloudTask(self, taskdata, result)

    def tasks(self,
              group: Optional[str] = None,
              *,
              index: int = 0,
              per: Optional[int] = None,
              option_fields: Optional[str] = None) -> TaskList:
        """Get tasks."""
        path = "v2/quantum-tasks/list"
        body = {
            "index": index,
        }  # type: dict[str, Any]
        if per is not None and per > 0:
            body["per"] = per
        if option_fields is not None:
            body["optionFileds"] = option_fields
        if group is not None:
            body["taskGroup"] = group
        tasks = self.post_request(path, body)
        tasks['tasks'] = [TaskData.from_dict(t) for t in tasks['tasks']]
        return TaskList(self,
                        tasklist=TaskListData(**tasks),
                        group=group,
                        index=index,
                        per=per,
                        option_fields=option_fields)

    def iter_tasks(self,
                   group: Optional[str] = None,
                   *,
                   index: int = 0,
                   per: Optional[int] = None,
                   option_fields: Optional[str] = None) -> TaskIter:
        """Get paginator of tasks"""
        return TaskIter(self,
                        group=group,
                        index=index,
                        per=per,
                        option_fields=option_fields)


def create_api(api_key: str) -> Api:
    """Create API from API key."""
    return Api(api_key)


def load_api(suffix: str = '') -> Api:
    """Load API from file."""
    key_path = _get_apikey_path(suffix)
    api_key = key_path.read_text().strip()
    return create_api(api_key)


def register_api(api_key: str, suffix: str = '') -> Api:
    """Save and return API."""
    api = Api(api_key)
    api.save_to_file(suffix)
    return api


def _check_suffix(suffix: str) -> bool:
    """Check validity of suffix"""
    return bool(re.match('^[-_a-zA-Z0-9]*$', suffix))


def _get_apikey_path(suffix: str) -> Path:
    if not _check_suffix(suffix):
        raise ValueError(f'Invalid suffix "{suffix}" is specified.')
    base = Path.home().joinpath(".bqcloud")
    if suffix:
        key_path = base.joinpath("api_key_" + suffix)
    else:
        key_path = base.joinpath("api_key")
    return key_path
