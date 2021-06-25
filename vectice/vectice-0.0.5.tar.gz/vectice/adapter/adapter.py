from __future__ import annotations

import logging
from abc import abstractmethod, ABC
from typing import List, Dict, Optional, Any

from vectice.api import Client
from vectice.models import Artifact, Job, JobRun, RunnableJob, ArtifactType, CodeVersionArtifact, JobRunStatus


class Run(dict):
    @abstractmethod
    def __enter__(self) -> dict:
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        pass


class AbstractAdapter(ABC):
    @property
    @abstractmethod
    def active_run(self) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def create_run(self, name: str) -> RunnableJob:
        pass

    @abstractmethod
    def end_run(self, outputs: Optional[List[Artifact]] = None) -> Optional[int]:
        pass

    @abstractmethod
    def start_run(self, inputs: Optional[List[Artifact]] = None) -> ActiveRun:
        pass

    @abstractmethod
    def save_job_and_associated_runs(self, name: str) -> None:
        pass

    @abstractmethod
    def save_run(
        self,
        run: Any,
        inputs: Optional[List[Artifact]] = None,
        outputs: Optional[List[Artifact]] = None,
    ) -> Optional[int]:
        pass


class ActiveRun(Run):
    """Wrapper around dict response to enable using Python ``with`` syntax."""

    def __init__(self, d: dict, adapter: AbstractAdapter):
        super().__init__(d)
        self._adapter = adapter

    def __enter__(self) -> dict:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._adapter.active_run:
            self._adapter.active_run["status"] = "COMPLETED" if exc_type is None else "FAILED"
        self._adapter.end_run()
        return exc_type is None


class Adapter(AbstractAdapter):
    def __init__(self, project_token: str, auto_connect=True):
        self._active_job = None
        self._client = Client(project_token, auto_connect)
        self._active_run: Optional[ActiveRun] = None
        self._active_inputs: List[Artifact] = []
        self._active_outputs: List[Artifact] = []
        self._runnable_job: Optional[RunnableJob] = None
        self._logger = logging.getLogger(self.__class__.__name__)

    @property
    def active_job(self) -> Optional[Dict[str, Any]]:
        return self._active_job

    @property
    def active_run(self) -> Optional[Dict[str, Any]]:
        return self._active_run

    @property
    def active_inputs(self) -> List[Artifact]:
        return self._active_inputs

    @property
    def active_outputs(self) -> List[Artifact]:
        return self._active_outputs

    def start_run(self, inputs: Optional[List[Artifact]] = None) -> ActiveRun:
        """
        start the run created before by calling create_run function
        :param inputs: list of artifacts used as inputs by this run.
        :return: a reference to a run executing
        """
        code_artifact_is_present = False
        if inputs is not None:
            for an_input in inputs:
                if an_input is not None:
                    an_input.jobArtifactType = "INPUT"
                    code_artifact_is_present = code_artifact_is_present or an_input.artifactType == ArtifactType.CODE
        if not code_artifact_is_present:
            if inputs is None:
                inputs = []
            artifact = CodeVersionArtifact.create(".")
            if artifact is not None:
                inputs.append(artifact)
        if self._runnable_job is None:
            raise RuntimeError("A job context must have been created.")
        response = self._client.start_run(self._runnable_job, inputs)
        self._active_job = response["job"]
        self._active_run = response["jobRun"]
        self._active_inputs = response["jobArtifacts"]
        self._active_outputs = []
        return ActiveRun(response, self)

    def end_run(self, outputs: Optional[List[Artifact]] = None) -> Optional[int]:
        """
        End the current (last) active run started by `start_run`.
        To end a specific run, use `stop_run` instead.
        """
        if self._active_run is None:
            self._logger.warning("No active run found.")
            return None
        if outputs is not None:
            for an_output in outputs:
                if an_output is not None:
                    an_output.jobArtifactType = "OUTPUT"
        self._active_run["status"] = "COMPLETED"
        self._client.stop_run(self._active_run, outputs)
        if self._active_run and "id" in self._active_run:
            run_id: Optional[int] = int(self._active_run["id"])
        else:
            run_id = None
        self._active_job = None
        self._active_run = None
        self._active_inputs = []
        self._active_outputs = []
        return run_id

    def __save_run(
        self,
        run: RunnableJob,
        inputs: Optional[List[Artifact]] = None,
        outputs: Optional[List[Artifact]] = None,
    ) -> Optional[int]:
        self._runnable_job = run
        self.start_run(inputs)
        return self.end_run(outputs)

    def save_job_and_associated_runs(self, name: str) -> None:
        raise RuntimeError("No implementation for this library")

    def save_run(
        self,
        run: Any,
        inputs: Optional[List[Artifact]] = None,
        outputs: Optional[List[Artifact]] = None,
    ) -> Optional[int]:
        """
        save run with its associated inputs and outputs.

        :param run:
        :param inputs:
        :param outputs:
        :return:
        """
        if isinstance(run, RunnableJob):
            return self.__save_run(run, inputs, outputs)
        else:
            raise RuntimeError("Incompatible object provided.")

    def create_run(self, job_name: str, job_type: Optional[str] = None) -> RunnableJob:
        """
        create an instance of a future run of a job.
        the run is not started. you need to start it by calling start_run

        :param job_type: the type of job. see :class:`~vectice.models.JobType` for the list of accepted type.
        :param job_name: the name of the job that should run.
        :return: an instance of a non started run.
        """
        if job_name is None:
            raise RuntimeError("Job name must be set")
        self._runnable_job = RunnableJob(Job(job_name, job_type), JobRun())
        return self._runnable_job

    def run_failed(self):
        self.__update_run_status(JobRunStatus.FAILED)

    def run_aborted(self):
        self.__update_run_status(JobRunStatus.ABORTED)

    def __update_run_status(self, status: str):
        if self._active_run is None or self._active_job is None:
            self._logger.warning("No active run found.")
            return
        self._active_run["status"] = status
        self._client.update_run(self._active_job["id"], self._active_run["id"], self._active_run)
