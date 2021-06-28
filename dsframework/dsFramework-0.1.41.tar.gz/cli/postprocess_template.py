 # !/usr/bin/env python
# coding: utf-8

from dsframework.base.pipeline.predictables.predictable import ZIDS_Predictable
from typing import List, Union

from dsframework.base.pipeline.postprocessor import ZIDS_Postprocessor
from pipeline.artifacts.shared_artifacts import generatedProjectNameSharedArtifacts
from pipeline.schema.outputs import generatedProjectNameOutputs

class generatedClass(ZIDS_Postprocessor):

    def __init__(self, artifacts: generatedProjectNameSharedArtifacts = None) -> None:
        super().__init__(artifacts)

    def config(self):
        pass

    def normalize_output(self, predictables: Union[ZIDS_Predictable, List[ZIDS_Predictable]]) -> Union[generatedProjectNameOutputs, List[generatedProjectNameOutputs]]:
        raise NotImplementedError
        # if predictables:
        #     # return generatedProjectNameOutputs(predictables)
