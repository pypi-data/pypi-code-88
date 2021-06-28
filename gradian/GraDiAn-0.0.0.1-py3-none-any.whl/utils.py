from typing import List

import spacy


def load_spacy_en_trf(excludes: List[str] = []):
    # Relies on en_core_web_trf SpaCy model
    try:
        nlp = spacy.load("en_core_web_trf", exclude=[excludes])
    except OSError as e:
        raise OSError('Try installing the model with "python -m spacy \
                      download en_core_web_trf', e)
    return nlp
