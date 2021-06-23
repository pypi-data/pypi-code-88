from typing import Dict
from typing import List
from typing import Tuple
from urllib.parse import urlparse

from pyspark.sql.types import TimestampType

from tecton._internals import errors
from tecton_proto.args.pipeline_pb2 import PipelineNode
from tecton_proto.common.id_pb2 import Id
from tecton_proto.data.materialization_status_pb2 import DataSourceType
from tecton_proto.data.materialization_status_pb2 import MaterializationAttemptStatus
from tecton_proto.data.materialization_status_pb2 import MaterializationStatusState
from tecton_spark.id_helper import IdHelper

_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def format_object_retrieval_arg(arg) -> str:
    if isinstance(arg, Id):
        res = f"'{IdHelper.to_string(arg)}'"
    else:
        res = repr(arg)
    return res


def validate_join_keys(join_keys: List[str]):
    """
    Validates that `join_keys` is not empty and has non-empty distinct values.

    :raises TectonValidationError: if `join_keys` is invalid.
    """
    if not join_keys:
        raise errors.EMPTY_ARGUMENT("join_keys")

    if "" in join_keys:
        raise errors.EMPTY_ELEMENT_IN_ARGUMENT("join_keys")

    if len(join_keys) > len(set(join_keys)):
        raise errors.DUPLICATED_ELEMENTS_IN_ARGUMENT("join_keys")


def validate_spine_dataframe(spine_df, timestamp_key):
    if spine_df is not None and timestamp_key:
        if timestamp_key not in spine_df.columns:
            raise errors.MISSING_SPINE_COLUMN("timestamp_key", timestamp_key, spine_df.columns)
        data_type = spine_df.schema[timestamp_key].dataType
        if not isinstance(data_type, TimestampType):
            raise errors.INVALID_SPINE_TIME_KEY_TYPE(data_type)


def parse_s3_path(path):
    """
    Returns (bucket, key) for an s3 URI
    """
    url = urlparse(path)
    return url.netloc, url.path.lstrip("/")


def format_seconds_into_highest_unit(total_seconds):
    intervals = [("wk", 60 * 60 * 24 * 7), ("d", 60 * 60 * 24), ("h", 60 * 60), ("m", 60), ("s", 1)]

    units = []
    for abbreviation, size in intervals:
        count = total_seconds // size
        total_seconds %= size
        if count != 0:
            units.append(f"{count}{abbreviation}")

    return " ".join(units[:2] if len(units) > 2 else units)


def snake_to_capitalized(snake_str):
    return "".join(x.title() for x in snake_str.split("_"))


def format_materialization_attempts(
    materialization_attempts, verbose=False, limit=1000, sort_columns=None, errors_only=False
) -> Tuple[List, List[List]]:
    """
    Formats a list of materialization attempts for use in Displayable.from_items
    Returns (column_names, materialization_status_rows).
    """
    column_names = ["TYPE", "WINDOW_START_TIME", "WINDOW_END_TIME", "STATUS", "ATTEMPT"]
    if verbose:
        column_names.extend(
            ["MATERIALIZATION_TASK", "ENV_VERSION", "TERMINATION_REASON", "STATE_MESSAGE", "TASK_SCHEDULED_AT"]
        )
    column_names.extend(["JOB_CREATED_AT", "JOB_LOGS"])

    materialization_attempts = materialization_attempts[:limit]
    if errors_only:
        materialization_attempts = [
            attempt
            for attempt in materialization_attempts
            if _materialization_status_state_name(attempt.materialization_state) == "ERROR"
        ]

    materialization_status_rows = []
    for attempt_status in materialization_attempts:
        data = _get_materialization_status_row_data(attempt_status)
        materialization_status_rows.append([data[c] for c in column_names])

    if sort_columns:
        keys = [k.upper() for k in sort_columns.split(",")]
        indices = []
        for key in keys:
            try:
                indices.append(column_names.index(key))
            except ValueError:
                raise ValueError(f"Unknown sort key {key}, should be one of: {','.join(column_names)}")
        materialization_status_rows.sort(key=lambda r: [r[i] for i in indices])

    return column_names, materialization_status_rows


def _materialization_status_state_name(state: MaterializationStatusState) -> str:
    state_name = MaterializationStatusState.Name(state)
    return state_name.replace("MATERIALIZATION_STATUS_STATE_", "")


def _get_materialization_status_row_data(attempt_status: MaterializationAttemptStatus) -> Dict[str, str]:
    status_dict = {}
    status_dict["TYPE"] = (
        "STREAM" if attempt_status.data_source_type == DataSourceType.DATA_SOURCE_TYPE_STREAM else "BATCH"
    )
    status_dict["WINDOW_START_TIME"] = (
        "N/A"
        if not attempt_status.HasField("window_start_time")
        else attempt_status.window_start_time.ToDatetime().strftime(_TIME_FORMAT)
    )
    status_dict["WINDOW_END_TIME"] = (
        "N/A"
        if not attempt_status.HasField("window_end_time")
        else attempt_status.window_end_time.ToDatetime().strftime(_TIME_FORMAT)
    )
    status_dict["STATUS"] = _materialization_status_state_name(attempt_status.materialization_state)
    status_dict["ATTEMPT"] = "N/A" if not attempt_status.HasField("attempt_number") else attempt_status.attempt_number
    status_dict["MATERIALIZATION_TASK"] = IdHelper.to_string(attempt_status.materialization_task_id)
    status_dict["ENV_VERSION"] = attempt_status.spark_cluster_environment_version
    status_dict["TERMINATION_REASON"] = (
        "N/A"
        if not attempt_status.HasField("termination_reason")
        or len(attempt_status.termination_reason) == 0
        or attempt_status.termination_reason == "UNKNOWN_TERMINATION_REASON"
        else attempt_status.termination_reason
    )
    status_dict["STATE_MESSAGE"] = (
        "N/A"
        if not attempt_status.HasField("state_message") or len(attempt_status.state_message) == 0
        else attempt_status.state_message
    )
    status_dict["TASK_SCHEDULED_AT"] = (
        "N/A"
        if not attempt_status.HasField("materialization_task_created_at")
        else attempt_status.materialization_task_created_at.ToDatetime().strftime(_TIME_FORMAT)
    )
    status_dict["JOB_CREATED_AT"] = (
        "N/A"
        if not attempt_status.HasField("attempt_created_at")
        else attempt_status.attempt_created_at.ToDatetime().strftime(_TIME_FORMAT)
    )
    status_dict["JOB_LOGS"] = "N/A" if not attempt_status.HasField("run_page_url") else attempt_status.run_page_url

    return status_dict


def get_num_dependent_fv(node: PipelineNode, visited_inputs: Dict[str, bool]) -> int:
    if node.HasField("feature_view_node"):
        if node.feature_view_node.input_name in visited_inputs:
            return 0
        visited_inputs[node.feature_view_node.input_name] = True
        return 1
    elif node.HasField("transformation_node"):
        ret = 0
        for child in node.transformation_node.inputs:
            ret = ret + get_num_dependent_fv(child.node, visited_inputs)
        return ret
    return 0
