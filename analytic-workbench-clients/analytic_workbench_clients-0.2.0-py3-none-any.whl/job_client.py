from typing import Dict, Any
from clients_core.service_clients import E360ServiceClient
from clients_core.exceptions import ClientValueError  # noqa: F401
from .models import JobCreateModel, JobModel, TaskStatusModel


class AWJobsClient(E360ServiceClient):
    """
    Subclasses dataclass `clients_core.service_clients.E360ServiceClient`.

    Args:
        client (clients_core.rest_client.RestClient): an instance of a rest client
        user_id (str): the user_id guid

    """
    service_endpoint = ""
    extra_headers = {"accept": "application/json"}

    def create(self, payload: Dict[str, Any], user_id: str, for_model: Dict[str, Any] = None, **kwargs: Any) -> JobModel:
        """
        Create a new AW job.

        Args:
            payload: job submission payload, as dict
            user_id: user_id, as str
            for_model: optional dict for the creation model
        Raises:
            pydantic.ValidationError: when the model creation fails validation

        """
        model = JobCreateModel(userId=user_id, payload=payload, **(for_model or {}))
        response = self.client.post('', json=model.dict(), raises=True, **kwargs)
        return JobModel.parse_obj(response.json())

    def get_by_id(self, job_id: str, **kwargs: Any) -> JobModel:
        url = f'{job_id}/'
        response = self.client.get(url, raises=True, **kwargs)
        return JobModel.parse_obj(response.json())

    def submit_job_by_id(self, job_id: str, **kwargs: Any) -> bool:
        url = f'{job_id}/submit/'
        response = self.client.post(url, raises=True, **kwargs)
        return response.ok

    def job_task_status_by_id(self, job_id: str, **kwargs: Any) -> TaskStatusModel:
        url = f'{job_id}/task/'
        response = self.client.get(url, raises=True, **kwargs)
        return TaskStatusModel.parse_obj(response.json())
