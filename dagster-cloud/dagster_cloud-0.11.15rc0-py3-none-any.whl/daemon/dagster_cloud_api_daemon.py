import logging
import sys
import time

import pendulum
from dagster import check
from dagster.core.events.log import EventLogEntry
from dagster.core.host_representation import (
    ExternalPipeline,
    ExternalPipelineOrigin,
    PipelineSelector,
)
from dagster.daemon.daemon import DagsterDaemon
from dagster.grpc.types import ExecuteStepArgs
from dagster.serdes import deserialize_json_to_dagster_namedtuple, serialize_dagster_namedtuple
from dagster.utils.error import serializable_error_info_from_exc_info
from dagster.utils.external import external_pipeline_from_location
from dagster_cloud.api.dagster_cloud_api import (
    CheckForWorkspaceUpdatesSuccess,
    DagsterCloudApi,
    DagsterCloudApiErrorResponse,
    DagsterCloudApiSuccess,
)
from dagster_cloud.executor.step_handler_context import DagsterCloudStepHandlerContext

GET_USER_CLOUD_REQUESTS_QUERY = """
    mutation GetUserCloudRequests {
        userCloudAgent {
            popUserCloudAgentRequests(limit:10) {
                requestBody
            }
        }
    }
"""

SEND_USER_CLOUD_RESPONSE_MUTATION = """
    mutation SendUserCloudResponse($requestId: String!, $requestApi: String!, $response: String!) {
        userCloudAgent {
            sendUserCloudAgentResponse(requestId: $requestId, requestApi: $requestApi, responseBody: $response) {
                requestId
            }
        }
    }
"""

WORKSPACE_ENTRIES_QUERY = """
    query WorkspaceEntries {
        workspace {
            workspaceEntries {
                serializedWorkspaceEntry
            }
        }
    }
"""


CLEAR_ERRORS_INTERVAL = 10


class DagsterCloudApiDaemon(DagsterDaemon):
    def __init__(self):
        self._initial_workspace_loaded = False
        super(DagsterCloudApiDaemon, self).__init__(interval_seconds=1)

    @classmethod
    def daemon_type(cls):
        return "DAGSTER_CLOUD_API"

    def __exit__(self, _exception_type, _exception_value, _traceback):
        self._cleanup()

    def __del__(self):
        self._cleanup()

    def _cleanup(self):
        pass

    def _check_for_workspace_updates(self, instance, workspace):
        workspace.cleanup()  # Clear any existing origins

        # Get list of workspace entries from DB
        result = instance.graphql_client.execute(WORKSPACE_ENTRIES_QUERY)
        entries = result["data"]["workspace"]["workspaceEntries"]

        # Create mapping of
        # - location name => deployment metadata
        deployment_map = {}
        force_update_locations = set()
        for entry in entries:
            workspace_entry = deserialize_json_to_dagster_namedtuple(
                entry["serializedWorkspaceEntry"]
            )
            deployment_map[workspace_entry.location_name] = workspace_entry.deployment_metadata
            if workspace_entry.outdated_data:
                force_update_locations.add(workspace_entry.location_name)

        workspace.grpc_server_registry.update_grpc_metadata(deployment_map, force_update_locations)

    def _get_repository_location(self, workspace, repository_location_origin):
        return workspace.get_location(repository_location_origin)

    def _get_external_repository_hierarchy(self, workspace, external_repository_origin):
        repository_location = self._get_repository_location(
            workspace, external_repository_origin.repository_location_origin
        )

        external_repository = repository_location.get_repository(
            external_repository_origin.repository_name
        )
        return (
            repository_location,
            external_repository,
        )

    def _get_external_pipeline_hierarchy(self, workspace, external_pipeline_origin):
        check.inst_param(
            external_pipeline_origin, "external_pipeline_origin", ExternalPipelineOrigin
        )
        external_repository_origin = external_pipeline_origin.external_repository_origin

        repository_location, external_repository = self._get_external_repository_hierarchy(
            workspace, external_repository_origin
        )

        return (
            repository_location,
            external_repository,
            external_repository.get_full_external_pipeline(external_pipeline_origin.pipeline_name),
        )

    def _handle_api_request(self, request, instance, workspace):
        api_name = request.request_api

        if api_name == DagsterCloudApi.CHECK_FOR_WORKSPACE_UPDATES:
            self._check_for_workspace_updates(instance, workspace)
            return CheckForWorkspaceUpdatesSuccess()
        elif api_name == DagsterCloudApi.GET_EXTERNAL_EXECUTION_PLAN:
            external_pipeline_origin = request.request_args.pipeline_origin

            (
                repository_location,
                external_repo,
                external_pipeline,
            ) = self._get_external_pipeline_hierarchy(workspace, external_pipeline_origin)

            if request.request_args.solid_selection:
                selector = PipelineSelector(
                    repository_location.name,
                    external_repo.name,
                    external_pipeline.name,
                    request.request_args.solid_selection,
                )
                subset_result = repository_location.get_subset_external_pipeline_result(selector)
                external_pipeline = ExternalPipeline(
                    subset_result.external_pipeline_data,
                    external_repo.handle,
                )

            return repository_location.get_external_execution_plan(
                external_pipeline=external_pipeline,
                run_config=request.request_args.run_config,
                mode=request.request_args.mode,
                step_keys_to_execute=request.request_args.step_keys_to_execute,
                known_state=request.request_args.known_state,
            ).execution_plan_snapshot

        elif api_name == DagsterCloudApi.GET_SUBSET_EXTERNAL_PIPELINE_RESULT:
            external_pipeline_origin = request.request_args.pipeline_origin
            (
                repository_location,
                external_repository,
                external_pipeline,
            ) = self._get_external_pipeline_hierarchy(workspace, external_pipeline_origin)
            return repository_location.get_subset_external_pipeline_result(
                PipelineSelector(
                    location_name=repository_location.name,
                    repository_name=external_repository.name,
                    pipeline_name=external_pipeline.name,
                    solid_selection=request.request_args.solid_selection,
                )
            )
        elif api_name == DagsterCloudApi.GET_EXTERNAL_PARTITION_CONFIG:
            external_repository_origin = request.request_args.repository_origin
            repository_location, external_repository = self._get_external_repository_hierarchy(
                workspace, external_repository_origin
            )
            return repository_location.get_external_partition_config(
                external_repository.handle,
                request.request_args.partition_set_name,
                request.request_args.partition_name,
            )
        elif api_name == DagsterCloudApi.GET_EXTERNAL_PARTITION_TAGS:
            external_repository_origin = request.request_args.repository_origin
            repository_location, external_repository = self._get_external_repository_hierarchy(
                workspace, external_repository_origin
            )
            return repository_location.get_external_partition_tags(
                external_repository.handle,
                request.request_args.partition_set_name,
                request.request_args.partition_name,
            )
        elif api_name == DagsterCloudApi.GET_EXTERNAL_PARTITION_NAMES:
            external_repository_origin = request.request_args.repository_origin
            repository_location, external_repository = self._get_external_repository_hierarchy(
                workspace, external_repository_origin
            )

            return repository_location.get_external_partition_names(
                external_repository.handle, request.request_args.partition_set_name
            )
        elif api_name == DagsterCloudApi.GET_EXTERNAL_PARTITION_SET_EXECUTION_PARAM_DATA:
            external_repository_origin = request.request_args.repository_origin
            repository_location, external_repository = self._get_external_repository_hierarchy(
                workspace, external_repository_origin
            )
            return repository_location.get_external_partition_set_execution_param_data(
                external_repository.handle,
                request.request_args.partition_set_name,
                request.request_args.partition_names,
            )
        elif api_name == DagsterCloudApi.GET_EXTERNAL_SCHEDULE_EXECUTION_DATA:
            external_repository_origin = request.request_args.repository_origin

            repository_location, external_repository = self._get_external_repository_hierarchy(
                workspace, external_repository_origin
            )
            scheduled_execution_time = (
                pendulum.from_timestamp(
                    request.request_args.scheduled_execution_timestamp,
                    tz=request.request_args.scheduled_execution_timezone,
                )
                if request.request_args.scheduled_execution_timestamp
                else None
            )
            return repository_location.get_external_schedule_execution_data(
                instance,
                external_repository.handle,
                request.request_args.schedule_name,
                scheduled_execution_time,
            )
        elif api_name == DagsterCloudApi.GET_EXTERNAL_SENSOR_EXECUTION_DATA:
            external_repository_origin = request.request_args.repository_origin

            repository_location, external_repository = self._get_external_repository_hierarchy(
                workspace, external_repository_origin
            )
            return repository_location.get_external_sensor_execution_data(
                instance,
                external_repository.handle,
                request.request_args.sensor_name,
                request.request_args.last_completion_time,
                request.request_args.last_run_key,
                request.request_args.cursor,
            )
        elif api_name == DagsterCloudApi.LAUNCH_RUN:
            run = request.request_args.pipeline_run
            instance.report_engine_event(
                f"Received request from {instance.dagster_cloud_url} to launch all steps for pipeline {run.pipeline_name}",
                run,
                cls=self.__class__,
            )
            repository_location = self._get_repository_location(
                workspace,
                run.external_pipeline_origin.external_repository_origin.repository_location_origin,
            )

            external_pipeline = external_pipeline_from_location(
                repository_location, run.external_pipeline_origin, run.solid_selection
            )

            launcher = workspace.grpc_server_registry.run_launcher()
            launcher.launch_run(run, external_pipeline)
            return DagsterCloudApiSuccess()
        elif api_name == DagsterCloudApi.LAUNCH_STEP:
            context = DagsterCloudStepHandlerContext.deserialize(
                instance, request.request_args.persisted_step_handler_context
            )
            args: ExecuteStepArgs = context.execute_step_args
            assert len(args.step_keys_to_execute) == 1
            step_key = args.step_keys_to_execute[0]

            instance.report_engine_event(
                f"Received request from {instance.dagster_cloud_url} to launch steps: {', '.join(args.step_keys_to_execute)}",
                context.pipeline_run,
                cls=self.__class__,
            )

            step_handler = workspace.grpc_server_registry.step_handler()
            events = step_handler.launch_step(context)
            for event in events:
                event_record = EventLogEntry(
                    message=event.message,
                    user_message=event.message,
                    level=logging.INFO,
                    pipeline_name=context.pipeline_run.pipeline_name,
                    run_id=context.pipeline_run.run_id,
                    error_info=None,
                    timestamp=time.time(),
                    step_key=step_key,
                    dagster_event=event,
                )
                instance.handle_new_event(event_record)

            return DagsterCloudApiSuccess()

        elif api_name == DagsterCloudApi.TERMINATE_STEP:
            context = DagsterCloudStepHandlerContext.deserialize(
                instance, request.request_args.persisted_step_handler_context
            )

            step_handler = workspace.grpc_server_registry.step_handler()
            events = step_handler.terminate_step(context)
            for event in events:
                instance.handle_new_event(event)

            return DagsterCloudApiSuccess()

        elif api_name == DagsterCloudApi.CHECK_STEP_HEALTH:
            context = DagsterCloudStepHandlerContext.deserialize(
                instance, request.request_args.persisted_step_handler_context
            )

            step_handler = workspace.grpc_server_registry.step_handler()
            events = step_handler.check_step_health(context)
            for event in events:
                instance.handle_new_event(event)

            return DagsterCloudApiSuccess()

        else:
            raise Exception(
                "Unexpected dagster cloud api call {api_name}".format(api_name=api_name)
            )

    def run_iteration(self, instance, workspace):
        if not self._initial_workspace_loaded:
            self._check_for_workspace_updates(instance, workspace)
            self._initial_workspace_loaded = True

        while True:
            result = instance.graphql_client.execute(GET_USER_CLOUD_REQUESTS_QUERY)

            requests = [
                deserialize_json_to_dagster_namedtuple(request["requestBody"])
                for request in result["data"]["userCloudAgent"]["popUserCloudAgentRequests"]
            ]

            for request in requests:
                self._logger.info(
                    "Responding to API request {request_id}: {request_name} with args: {request_args}".format(
                        request_id=request.request_id,
                        request_name=request.request_api,
                        request_args=str(request.request_args) if request.request_args else "None",
                    )
                )

                api_result = None
                try:
                    api_result = self._handle_api_request(request, instance, workspace)
                except Exception:  # pylint: disable=broad-except
                    error_info = serializable_error_info_from_exc_info(sys.exc_info())
                    api_result = DagsterCloudApiErrorResponse(error_infos=[error_info])
                    self._logger.error(
                        "Error serving API request {request_id}: {request_name}:\n{error_info}".format(
                            request_id=request.request_id,
                            request_name=request.request_api,
                            error_info=str(error_info),
                        )
                    )
                    yield error_info

                response = serialize_dagster_namedtuple(api_result)

                # Check for errors
                instance.graphql_client.execute(
                    SEND_USER_CLOUD_RESPONSE_MUTATION,
                    {
                        "requestId": request.request_id,
                        "requestApi": request.request_api.value,
                        "response": response,
                    },
                )

            time.sleep(0.5)
            yield
