import logging
from pathlib import Path
from typing import Callable
from typing import Optional

from dkist_processing_core.task import TaskBase

from dkist_processing_common.tasks.base import WorkflowDataTaskBase


class ManualProcessing:
    def __init__(self, workflow_path: Path, recipe_run_id: Optional[int] = 1):
        self.workflow_path = workflow_path
        self.recipe_run_id = recipe_run_id

    def run_task(self, task: Callable) -> None:
        """
        Wrapper function for calling the .run() method on a DKIST processing pipeline task
        Parameters
        ----------
        task: Callable
            task object that subclasses TaskBase
        Returns
        -------
        None
        """
        if not issubclass(task, TaskBase):
            raise RuntimeError(
                "Task is not a valid DKIST processing task. "
                "Must be a subclass of dkist_processing_core.task.TaskBase"
            )
        t = task(
            recipe_run_id=self.recipe_run_id, workflow_name="manual", workflow_version="manual"
        )
        t.scratch.scratch_base_path = self.workflow_path
        t.run()
        logging.info(f"Task {task.__name__} completed")

    def purge_tags_and_constants(self) -> None:
        """
        Remove all filepath tags and constants from the associated objects.
        Run at the end of a manual processing run.
        Returns
        -------
        None
        """

        class PurgeTagsAndConstants(WorkflowDataTaskBase):
            def run(self):
                pass

        t = PurgeTagsAndConstants(
            recipe_run_id=self.recipe_run_id, workflow_name="manual", workflow_version="manual"
        )
        t.scratch._tag_db.purge()
        t.constants.purge()
        logging.info(f"Constants and filepath tags purged for recipe run id {self.recipe_run_id}")
