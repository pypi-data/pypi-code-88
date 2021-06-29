import logging
import re

from ariadne.classifier import Classifier
from .inception_util import create_prediction
from cassis import Cas

_the_re = re.compile(r'\bthe\b', re.IGNORECASE)
_logger = logging.getLogger("the_classifier")


class TheClassifier(Classifier):
    """
    Classifier marks all 'the' in the text
    """
    def __init__(self, value_str: str = 'the'):
        super().__init__()
        self.value_str = value_str

    def predict(self, cas: Cas, layer: str, feature: str, project_id: str, document_id: str, user_id: str):
        _logger.info(f"Got predict query: layer='{layer}', feature='{feature}', project_id: '{project_id}', "
                     f"document_id: {document_id}, user_id: {document_id}")
        text = cas.sofa_string
        for m in _the_re.finditer(text):
            pos = m.span()
            prediction = create_prediction(cas, layer, feature, pos[0], pos[1], self.value_str)
            cas.add_annotation(prediction)
