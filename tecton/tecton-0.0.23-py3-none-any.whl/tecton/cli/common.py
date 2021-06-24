import inspect
from pathlib import Path

from tecton import conf
from tecton._internals.workspace_utils import PROD_WORKSPACE_NAME_CLIENT
from tecton_proto.args.repo_metadata_pb2 import SourceInfo


def get_current_workspace():
    workspace_name = conf.get("TECTON_WORKSPACE")
    if not workspace_name:
        return PROD_WORKSPACE_NAME_CLIENT
    return workspace_name


def get_fco_source_info() -> SourceInfo:
    from tecton.cli.cli import _repo_root

    source_info = SourceInfo()
    if not _repo_root:
        pass
    else:
        frames = inspect.stack()
        repo_root_path = Path(_repo_root)
        for frame in frames:
            frame_path = Path(frame.frame.f_code.co_filename).resolve()
            if frame_path.exists() and (repo_root_path in frame_path.parents):
                rel_filename = frame_path.relative_to(repo_root_path)
                source_info.source_lineno = str(frame.lineno)
                source_info.source_filename = str(rel_filename)
                break
    return source_info


def is_materializable_workspace(workspace_name: str) -> bool:
    return workspace_name == PROD_WORKSPACE_NAME_CLIENT
