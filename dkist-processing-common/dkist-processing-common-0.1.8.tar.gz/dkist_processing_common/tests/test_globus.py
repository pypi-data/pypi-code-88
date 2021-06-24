from pathlib import Path

import pytest

from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.tasks.base import WorkflowDataTaskBase
from dkist_processing_common.tasks.mixin.globus import GlobusMixin


class GlobusTask(WorkflowDataTaskBase, GlobusMixin):
    def run(self):
        pass


@pytest.fixture(scope="function")
def globus_task(tmp_path, recipe_run_id):
    with GlobusTask(
        recipe_run_id=recipe_run_id,
        workflow_name="workflow_name",
        workflow_version="workflow_version",
    ) as task:
        task.scratch = WorkflowFileSystem(
            recipe_run_id=recipe_run_id,
            scratch_base_path=tmp_path,
        )
        task.scratch.workflow_base_path = tmp_path / str(recipe_run_id)
        yield task
        task.scratch.purge()
        task.constants.purge()


def test_good_globus_path(globus_task):
    """
    Given: A GlobusTask mixin
    When: Resolving the globus path with a base that is relative to the workflow base path
    Then: The path is correctly truncated
    """
    assert globus_task.globus_path(globus_task.scratch.workflow_base_path) == Path(
        str(globus_task.recipe_run_id)
    )
