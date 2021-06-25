from typing import Any, List, Optional, Dict

from vectice.api.Page import Page
from vectice.api.dataset import DatasetApi
from vectice.api.dataset_version import DatasetVersionApi
from vectice.api.job import JobApi
from vectice.api.job_artifact import ArtifactApi
from vectice.api.job_run import RunApi
from vectice.api.model import ModelApi
from vectice.api.model_version import ModelVersionApi
from vectice.api.output.job_output import JobOutput
from vectice.api.output.job_run_output import JobRunOutput
from vectice.api.output.paged_response import PagedResponse
from vectice.api.project import ProjectApi
from vectice.api.rule import RuleApi
from vectice.models import Artifact, RunnableJob


class Client(ProjectApi):
    """
    Low level Vectice API client.
    """

    def __init__(self, project_token: str, auto_connect=True):
        super().__init__(project_token=project_token, auto_connect=auto_connect)
        self._api_config = {
            "project_token": self.project_token,
            "_token": self._token,
        }

    @property
    def _config(self) -> dict:
        self._api_config["_token"] = self._token
        return self._api_config

    def start_run(
        self,
        run: RunnableJob,
        inputs: Optional[List[Artifact]] = None,
    ):
        return RuleApi(**self._config).start_run(run.job, run.run, inputs)

    def stop_run(self, run: Dict[str, Any], outputs: Optional[List[Artifact]] = None):
        return RuleApi(**self._config).stop_run(run, outputs)

    def list_jobs(
        self, search: Optional[str] = None, page_index=Page.index, page_size=Page.size
    ) -> PagedResponse[JobOutput]:
        return JobApi(**self._config).list_jobs(search, page_index, page_size)

    def create_job(self, job: Dict[str, str]) -> JobOutput:
        """
        create a job
        :param job: a job description (json)
        :return: a JobOutput instance
        """
        return JobApi(**self._config).create_job(job)

    def update_job(self, job_id: int, job: dict):
        """
        update a job
        :param job: a job description (json)
        :return: the json structure
        """
        return JobApi(**self._config).update_job(job_id, job)

    def list_runs(self, job_id: int, page_index=Page.index, page_size=Page.size) -> List[JobRunOutput]:
        """
        list runs of a specific job.
        :param job_id:
        :param page_index:
        :param page_size:
        :return: a list of JobRunOutput
        """
        return RunApi(job_id=job_id, **self._config).list_runs(page_index, page_size)

    def create_run(self, job_id: int, run: dict):
        """
        create a run
        :param job_id:
        :param run:
        :return:
        """
        return RunApi(job_id=job_id, **self._config).create_run(run)

    def update_run(self, job_id: int, run_id: int, run: dict):
        """
        update a run
        :param job_id:
        :param run_id:
        :param run:
        :return:
        """
        return RunApi(job_id=job_id, **self._config).update_run(run_id, run)

    def create_artifact(self, job_id: int, run_id: int, artifact: dict):
        """
        create artifact
        :param job_id:
        :param run_id:
        :param artifact:
        :return:
        """
        return ArtifactApi(job_id=job_id, run_id=run_id, **self._config).create_artifact(artifact)

    def update_artifact(self, job_id: int, run_id: int, artifact_id: int, artifact: dict):
        """
        update artifact
        :param job_id:
        :param run_id:
        :param artifact_id:
        :param artifact:
        :return:
        """
        return ArtifactApi(job_id=job_id, run_id=run_id, **self._config).update_artifact(artifact_id, artifact)

    def list_datasets(self, search: str = None, page_index=Page.index, page_size=Page.size):
        """
        list datasets
        :param search:
        :param page_index:
        :param page_size:
        :return:
        """
        return DatasetApi(**self._config).list_datasets(search, page_index, page_size)

    def create_dataset(self, dataset: dict):
        return DatasetApi(**self._config).create_dataset(dataset)

    def update_dataset(self, dataset_id: int, dataset: dict):
        return DatasetApi(**self._config).update_dataset(dataset_id, dataset)

    def list_models(self, search: str = None, page_index=Page.index, page_size=Page.size):
        """
        list models
        :param search:
        :param page_index:
        :param page_size:
        :return:
        """
        return ModelApi(**self._config).list_models(search, page_index, page_size)

    def create_model(self, model: dict):
        return ModelApi(**self._config).create_model(model)

    def update_model(self, model_id: int, model: dict):
        return ModelApi(**self._config).update_model(model_id, model)

    def list_dataset_versions(self, dataset_id: int, page_index=Page.index, page_size=Page.size):
        return DatasetVersionApi(dataset_id=dataset_id, **self._config).list_dataset_versions(page_index, page_size)

    def create_dataset_version(self, dataset_id: int, dataset_version: dict):
        return DatasetVersionApi(dataset_id=dataset_id, **self._config).create_dataset_version(dataset_version)

    def update_dataset_version(self, dataset_id: int, dataset_version_id: int, dataset_version: dict):
        return DatasetVersionApi(dataset_id=dataset_id, **self._config).update_dataset_version(
            dataset_version_id, dataset_version
        )

    def list_model_versions(self, model_id: int, page_index=Page.index, page_size=Page.size):
        return ModelVersionApi(model_id=model_id, **self._config).list_model_versions(page_index, page_size)

    def create_model_version(self, model_id: int, model_version: dict):
        return ModelVersionApi(model_id=model_id, **self._config).create_model_version(model_version)

    def update_model_version(self, model_id: int, model_version_id: int, model_version: dict):
        return ModelVersionApi(model_id=model_id, **self._config).update_model_version(model_version_id, model_version)
