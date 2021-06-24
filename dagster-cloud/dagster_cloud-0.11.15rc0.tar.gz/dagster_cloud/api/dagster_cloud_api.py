from collections import namedtuple
from datetime import timedelta
from enum import Enum

import pendulum
from dagster import check
from dagster.core.code_pointer import CodePointer
from dagster.core.host_representation import ExternalRepositoryData, RepositoryLocationOrigin
from dagster.core.storage.pipeline_run import PipelineRun
from dagster.serdes import whitelist_for_serdes
from dagster.utils.error import SerializableErrorInfo
from dagster_cloud.executor.step_handler_context import PersistedDagsterCloudStepHandlerContext
from dagster_cloud.workspace.origin import CodeDeploymentMetadata

DEFAULT_EXPIRATION_MILLISECONDS = 10 * 60 * 1000


@whitelist_for_serdes
class DagsterCloudWorkspaceEntryStatus(Enum):
    LOADING = "LOADING"
    LOADED = "LOADED"
    ERRORED = "ERRORED"


@whitelist_for_serdes
class DagsterCloudWorkspaceEntry(
    namedtuple(
        "_DagsterCloudWorkspaceEntry",
        "location_name deployment_metadata load_repositories_response serialized_error_info timestamp data_updated_timestamp",
    )
):
    """Includes information to tell the daemon how to spin up a new location - both the
    RepositoryLocationOrigin (which uniquely identifies the location) and any additional information
    that might be needed to create the user code deployment (for example, the docker image
    to use). The daemon then populates the entry with repository information or an error message after
    spinning the location up."""

    def __new__(
        cls,
        location_name,
        deployment_metadata,
        load_repositories_response=None,
        serialized_error_info=None,
        timestamp=None,
        data_updated_timestamp=None,
    ):
        return super(DagsterCloudWorkspaceEntry, cls).__new__(
            cls,
            check.str_param(location_name, "location_name"),
            check.opt_inst_param(
                deployment_metadata, "deployment_metadata", CodeDeploymentMetadata
            ),
            check.opt_inst_param(
                load_repositories_response, "load_repositories_response", LoadRepositoriesResponse
            ),
            check.opt_inst_param(
                serialized_error_info, "serialized_error_info", SerializableErrorInfo
            ),
            check.opt_float_param(
                timestamp,
                "timestamp",
            ),
            check.opt_float_param(
                data_updated_timestamp,
                "data_updated_timestamp",
            ),
        )

    def with_load_repositories_response(self, load_repositories_response):
        check.inst_param(
            load_repositories_response, "load_repositories_response", LoadRepositoriesResponse
        )
        return self._replace(
            load_repositories_response=load_repositories_response,
            serialized_error_info=None,
        )

    def with_serialized_error_info(self, serialized_error_info):
        check.inst_param(serialized_error_info, "serialized_error_info", SerializableErrorInfo)
        return self._replace(
            load_repositories_response=None,
            serialized_error_info=serialized_error_info,
        )

    def with_timestamp(self, timestamp):
        check.float_param(timestamp, "timestamp")
        return self._replace(
            timestamp=timestamp,
        )

    @property
    def outdated_data(self):
        return self.data_updated_timestamp and self.timestamp > self.data_updated_timestamp

    @property
    def status(self):
        outdated_data = self.timestamp and self.outdated_data
        if not outdated_data and self.load_repositories_response:
            return DagsterCloudWorkspaceEntryStatus.LOADED
        elif not outdated_data and self.serialized_error_info:
            return DagsterCloudWorkspaceEntryStatus.ERRORED
        else:
            return DagsterCloudWorkspaceEntryStatus.LOADING

    def get_display_metadata(self):
        metadata = {
            "python_file": self.deployment_metadata.python_file,
            "package_name": self.deployment_metadata.package_name,
            "image": self.deployment_metadata.image,
        }
        return {key: value for key, value in metadata.items() if value is not None}


@whitelist_for_serdes
class DagsterCloudApi(Enum):
    CHECK_FOR_WORKSPACE_UPDATES = "CHECK_FOR_WORKSPACE_UPDATES"
    LOAD_REPOSITORIES = "LOAD_REPOSITORIES"
    GET_EXTERNAL_EXECUTION_PLAN = "GET_EXTERNAL_EXECUTION_PLAN"
    GET_SUBSET_EXTERNAL_PIPELINE_RESULT = "GET_SUBSET_EXTERNAL_PIPELINE_RESULT"
    GET_EXTERNAL_PARTITION_CONFIG = "GET_EXTERNAL_PARTITION_CONFIG"
    GET_EXTERNAL_PARTITION_TAGS = "GET_EXTERNAL_PARTITION_TAGS"
    GET_EXTERNAL_PARTITION_NAMES = "GET_EXTERNAL_PARTITION_NAMES"
    GET_EXTERNAL_PARTITION_SET_EXECUTION_PARAM_DATA = (
        "GET_EXTERNAL_PARTITION_SET_EXECUTION_PARAM_DATA"
    )
    GET_EXTERNAL_SCHEDULE_EXECUTION_DATA = "GET_EXTERNAL_SCHEDULE_EXECUTION_DATA"
    GET_EXTERNAL_SENSOR_EXECUTION_DATA = "GET_EXTERNAL_SENSOR_EXECUTION_DATA"

    LAUNCH_RUN = "LAUNCH_RUN"
    LAUNCH_STEP = "LAUNCH_STEP"
    CHECK_STEP_HEALTH = "CHECK_STEP_HEALTH"
    TERMINATE_STEP = "TERMINATE_STEP"


@whitelist_for_serdes
class DagsterCloudApiSuccess(namedtuple("_DagsterCloudApiSuccess", "")):
    pass


@whitelist_for_serdes
class CheckForWorkspaceUpdatesSuccess(namedtuple("_CheckForWorkspaceUpdatesSuccess", "")):
    pass


@whitelist_for_serdes
class LoadRepositoriesArgs(namedtuple("_LoadRepositoryArgs", "location_origin")):
    def __new__(cls, location_origin):
        return super(cls, LoadRepositoriesArgs).__new__(
            cls,
            check.inst_param(location_origin, "location_origin", RepositoryLocationOrigin),
        )


@whitelist_for_serdes
class DagsterCloudRepositoryData(
    namedtuple("_DagsterCloudRepositoryData", "repo_name code_pointer external_repository_data")
):
    def __new__(cls, repo_name, code_pointer, external_repository_data):
        return super(cls, DagsterCloudRepositoryData).__new__(
            cls,
            check.str_param(repo_name, "repo_name"),
            check.inst_param(code_pointer, "code_pointer", CodePointer),
            check.inst_param(
                external_repository_data,
                "external_repository_data",
                ExternalRepositoryData,
            ),
        )


@whitelist_for_serdes
class LoadRepositoriesResponse(
    namedtuple("_LoadRepositoriesResponse", "repository_datas container_image executable_path")
):
    def __new__(cls, repository_datas, container_image, executable_path):
        return super(cls, LoadRepositoriesResponse).__new__(
            cls,
            check.list_param(
                repository_datas,
                "repository_datas",
                of_type=DagsterCloudRepositoryData,
            ),
            check.opt_str_param(container_image, "container_image"),
            check.opt_str_param(executable_path, "executable_path"),
        )


@whitelist_for_serdes
class DagsterCloudApiErrorResponse(namedtuple("DagsterCloudApiErrorResponse", "error_infos")):
    def __new__(cls, error_infos):
        return super(cls, DagsterCloudApiErrorResponse).__new__(
            cls,
            check.list_param(error_infos, "error_infos", of_type=SerializableErrorInfo),
        )


@whitelist_for_serdes
class LaunchRunArgs(namedtuple("_LaunchRunArgs", "pipeline_run")):
    def __new__(cls, pipeline_run):
        return super(cls, LaunchRunArgs).__new__(
            cls,
            check.inst_param(pipeline_run, "pipeline_run", PipelineRun),
        )


@whitelist_for_serdes
class StepHandlerArgs(namedtuple("_StepHandlerArgs", "persisted_step_handler_context")):
    def __new__(cls, persisted_step_handler_context: PersistedDagsterCloudStepHandlerContext):
        return super(cls, StepHandlerArgs).__new__(
            cls,
            check.inst_param(
                persisted_step_handler_context,
                "persisted_step_handler_context",
                PersistedDagsterCloudStepHandlerContext,
            ),
        )


@whitelist_for_serdes
class DagsterCloudApiRequest(
    namedtuple("_DagsterCloudApiRequest", "request_id request_api request_args expire_at")
):
    def __new__(
        cls,
        request_id,
        request_api,
        request_args,
        expire_at=None,
    ):
        return super(cls, DagsterCloudApiRequest).__new__(
            cls,
            check.str_param(request_id, "request_id"),
            check.inst_param(request_api, "request_api", DagsterCloudApi),
            request_args,
            check.opt_float_param(
                expire_at,
                "expire_at",
                default=(
                    pendulum.now("UTC") + timedelta(milliseconds=DEFAULT_EXPIRATION_MILLISECONDS)
                ).timestamp(),
            ),
        )

    @property
    def is_expired(self):
        return pendulum.now("UTC").timestamp() > self.expire_at
