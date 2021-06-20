 # !/usr/bin/env python
# coding: utf-8

from dsFramework.base.pipeline.predictables.predictable import ZIDS_Predictable
from typing import List, Any

from dsFramework.base.pipeline.postprocessor import ZIDS_Postprocessor
from generatedPipelineDir.artifacts.shared_artifacts import generatedProjectNameSharedArtifacts
from generatedPipelineDir.schema.outputs import generatedProjectNameOutputs

class generatedClass(ZIDS_Postprocessor):

    def __init__(self, artifacts: generatedProjectNameSharedArtifacts = None) -> None:
        super().__init__(artifacts)

    def config(self):
        pass

    def normalize_output(self, predictables: List[ZIDS_Predictable]) -> Any:
        raise NotImplementedError
        # if predictables:
        #     # return generatedProjectNameOutputs(predictables)
