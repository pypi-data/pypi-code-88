import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from dsFramework.base.pipeline.pipeline import ZIDS_Pipeline
from dsFramework.base.common.component import ZIDS_Component

from generatedDirectory.preprocessor.preprocess import generatedProjectNamePreprocess
from generatedDirectory.postprocessor.postprocess import generatedProjectNamePostprocess
from generatedDirectory.predictors.predictor import generatedProjectNamePredictor
from generatedDirectory.forcers.forcer import generatedProjectNameForcer
from generatedDirectory.artifacts.shared_artifacts import generatedProjectNameSharedArtifacts

class generatedClass(ZIDS_Pipeline):

    def __init__(self):
        super().__init__()

    def get_artifacts(self):
        return generatedProjectNameSharedArtifacts()

    def build_pipeline(self):
        self.preprocessor  = generatedProjectNamePreprocess(artifacts = self.artifacts)
        self.postprocessor = generatedProjectNamePostprocess(artifacts = self.artifacts)
        self.predictor = generatedProjectNamePredictor()
        self.forcer = generatedProjectNameForcer()
        self.add_component(self.predictor)
        self.add_component(self.forcer)

    def preprocess(self, **kwargs):
        return self.preprocessor(**kwargs)

    def postprocess(self, predictables):
        return self.postprocessor(predictables)
