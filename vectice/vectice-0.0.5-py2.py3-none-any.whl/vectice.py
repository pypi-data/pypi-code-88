import logging
from typing import Optional, Any, List, Sequence

from vectice.adapter import Adapter
from vectice.api import Page
from vectice.api.output import JobOutput, JobRunOutput, PagedResponse
from vectice.models import (
    Artifact,
    RunnableJob,
    Job,
    JobRun,
    DatasetVersionArtifact,
    Artifacts,
    ModelVersionArtifact,
    CodeVersionArtifact,
)

logger = logging.getLogger(__name__)


# Import experiment into Vectice with all associated run (could be long !)
def save_job(project_token: str, experiment_name: str, lib: str):
    try:
        vectice = Vectice(project_token=project_token, lib=lib)
        vectice.save_job_and_associated_runs(experiment_name)
    except Exception:
        logger.exception(f"saving job {experiment_name} failed")


# Import run of experiment into Vectice
def save_after_run(
    project_token: str,
    run: Any,
    lib: Optional[str],
    inputs: Optional[List[Artifact]] = None,
    outputs: Optional[List[Artifact]] = None,
) -> Optional[int]:
    """
        save in Vectice platform information relative to this run.
        The run object can be of several type depending on which
        lib you are using.

    :param project_token:
    :param run: the run we want to save
    :param lib: Name of the lib you are using (for now, None or MLFlow)
    :param inputs: list of inputs (artifact) you are using in this run
    :param outputs: list of outputs (artifact) you are using in this run
    :return: id of the saved run or None if the run can not be saved
    """
    try:
        vectice = Vectice(project_token, lib)
        return vectice.save_run(run, inputs, outputs)
    except Exception:
        logger.exception("saving run failed")
        return None


def create_run(job_name: str, job_type: Optional[str] = None) -> RunnableJob:
    """
    create a runnable job. This object will save any information relative
    to a run and its associated job.

    :param job_name: the name of the job involve in the run
    :param job_type: the type of the job involve in the run
    :return:
    """
    if job_name is None:
        raise RuntimeError("Name of job must be provided.")
    job = Job(job_name)
    if job_type is not None:
        job.with_type(job_type)
    return RunnableJob(job, JobRun())


class Vectice(Adapter):
    """
    High level class to list jobs and runs but also save runs
    """

    def __new__(cls, project_token: str, lib: str = None, *args, **kwargs):
        if lib is not None:
            if str(lib).lower() == "mlflow":
                from vectice.adapter.mlflow import MlflowAdapter

                return MlflowAdapter(project_token=project_token, *args, **kwargs)  # type: ignore
            else:
                raise ValueError(f"Unsupported lib: {lib}")
        else:
            return super().__new__(cls)

    def __init__(self, project_token: str, lib: Optional[str] = None):
        super().__init__(project_token=project_token)

    def list_jobs(
        self, search: Optional[str] = None, page_index=Page.index, page_size=Page.size
    ) -> PagedResponse[JobOutput]:
        """
        list all jobs
        :param search:
        :param page_index:
        :param page_size:
        :return:
        """
        return self._client.list_jobs(search, page_index, page_size)

    def list_runs(self, job_id: int, page_index=Page.index, page_size=Page.size) -> Sequence[JobRunOutput]:
        """
        list all run of a specific job
        :param job_id: the Vectice job identifier
        :param page_index:
        :param page_size:
        :return:
        """
        return self._client.list_runs(job_id, page_index, page_size)

    @classmethod
    def create_dataset_version(cls, description: Optional[str] = None) -> DatasetVersionArtifact:
        """
        create an artifact that contains a version of a dataset
        :param path:
        :return:
        """
        return Artifacts.create_dataset_version(description)

    @classmethod
    def create_model_version(cls, description: Optional[str] = None) -> ModelVersionArtifact:
        """
        create an artifact that contains a version of a model
        :param path:
        :return:
        """
        return Artifacts.create_model_version(description)

    @classmethod
    def create_code_version(cls, path: str = ".") -> Optional[CodeVersionArtifact]:
        """
        create an artifact that contains a version of a code
        :param path:
        :return:
        """
        return Artifacts.create_code_version(path)

    @classmethod
    def prepare_run(cls, job_name: str, job_type: Optional[str] = None) -> RunnableJob:
        return create_run(job_name, job_type)

    @classmethod
    def save_after_run(
        cls,
        project_token: str,
        run: Any,
        lib: Optional[str],
        inputs: Optional[List[Artifact]] = None,
        outputs: Optional[List[Artifact]] = None,
    ) -> Optional[int]:
        return save_after_run(project_token, run, lib, inputs, outputs)
