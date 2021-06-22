#!python

import json
import os
import sys
import traceback
from typing import Dict, Any

from quixote import new_context
from quixote.inspection import new_inspection_result, CriticalFailureError

from panza.internals.blueprint import augmented_syspath, BlueprintLoader
from panza.internals.workspace import WorkspaceLayout, EXECUTOR_WORKSPACE_ROOT
from panza.internals.result_serialization import serialize_result

workspace = WorkspaceLayout(EXECUTOR_WORKSPACE_ROOT)

os.chdir(workspace.work_directory)

with open(workspace.context_file, 'r') as context_file:
    context: Dict[str, Any] = json.load(context_file)

os.remove(workspace.context_file)

job_failure = None
job_result = None

with augmented_syspath([workspace.moulinette_directory]):
    with new_context(
            resources_path=workspace.resources_directory,
            delivery_path=workspace.delivery_directory,
            **context
    ):
        blueprint = BlueprintLoader.load_from_directory(
            workspace.moulinette_directory,
            complete_load=True
        )

        print(f"Running inspectors for {blueprint.name}")
        with new_inspection_result() as result:
            for inspector in blueprint.inspectors:
                try:
                    inspector()
                except CriticalFailureError:
                    print("Critical step failure, skipping remaining inspectors")
                    break
                except Exception as e:
                    print(f"Unexpected exception escaped from inspector: {type(e).__name__}: {e}")
                    traceback.print_exc(file=sys.stdout)
                    job_failure = e
                    break
            job_result = result

with open(workspace.result_file, 'w') as f:
    if job_failure is not None:
        result = {"error": {"message": str(job_failure)}}
    else:
        result = {"success": {"result": job_result}}
    serialize_result(result, f)

print("Done")
